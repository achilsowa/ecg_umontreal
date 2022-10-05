import os
import numpy as np
import matplotlib.pyplot as plt
import config

path_to_output = f"{os.getcwd()}/{config.STATIC_DIR}/"
if not os.path.exists(path_to_output):
    os.mkdir(path_to_output)


def get_filename(row):
    AcquisitionDateTime = (
        row["AcquisitionDate"] + "_" + row["AcquisitionTime"].replace(":", "-")
    )

    return f"{row['patientid']}_{AcquisitionDateTime}.png"


def already_plotted(row):
    filename = get_filename(row)
    file_output = path_to_output + filename
    return os.path.exists(file_output)


def plot(row):

    path = os.path.join(row["ecg_output_path"])
    file = np.load(path)
    file = np.reshape(file, (1, 2500, 12))

    # To reconstruct the 12 lead ecg from the array
    lead_order = [
        "I",
        "II",
        "III",
        "aVR",
        "aVL",
        "aVF",
        "V1",
        "V2",
        "V3",
        "V4",
        "V5",
        "V6",
    ]
    plt.rcParams["figure.figsize"] = [16, 9]
    # Do not display plot in notebook
    # plt.ioff()
    fig, axs = plt.subplots(len(lead_order))
    for i in range(12):
        if i == 0:
            axs[i].set_title(f"ECG patient: {row['patientid']}")

        axs[i].plot(file[0][:, i])
        axs[i].set(ylabel=str(lead_order[i]))

    # Save plt to JPEG
    filename = get_filename(row)

    file_output = path_to_output + filename

    plt.savefig(file_output, dpi=300, bbox_inches="tight")
    return filename
