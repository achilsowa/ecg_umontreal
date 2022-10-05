import os
import csv
from urllib.parse import urlparse, parse_qs
from lib import plot_lib
from .utils import get_header, get_body
import config


"""
Patient page. Get the patient id from the url query, and if the image does not yet exist, plot the ecg image for the given 
patient. 
"""


def view(server):
    src_data = os.getcwd() + config.PATIENT_CSV
    qs = parse_qs(urlparse(server.path).query)
    patientid = qs.get('patientid')[0]
    content = ""
    with open(src_data, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['patientid'] == patientid:
                content += ""
                img_src = f"/{config.STATIC_DIR}/{plot_lib.get_filename(row)}"

                # We draw the image only the first time
                if not plot_lib.already_plotted(row):
                    plot_lib.plot(row)
                content += f"<h5> <a href='/'>&lt Retour</a></h5>"
                content += f"<h4 class='text-center'>Patient {row['patientid']}</h4>"
                content += f"<img class='card-img-bottom' src='{img_src}' />"

    server.send_response(200)
    server.send_header("Content-type", "text/html")
    server.end_headers()

    head = get_header("Patient")
    body = get_body(content)
    server.wfile.write(
        bytes(f"<html>{head} {body}</html>", "utf-8"))
