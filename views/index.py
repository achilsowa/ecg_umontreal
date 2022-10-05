import os
import csv
from .utils import get_header, get_body
import config

"""
Home page, list the patients in a select box and add a button to show the selected patient ecg
"""


def view(server):
    content = "<form class='form-row' method='get' action='/'> <div class='col-md-8 mb-2'>"
    content += "<select class='form-control form-control-lg' name='patientid'>"
    content += "<option value selected>Selectionner un patient id</option>"

    src_data = os.getcwd() + config.PATIENT_CSV
    with open(src_data, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content += f"<option value='{row['patientid']}'>Patient {row['patientid']}</option>"
    content += "</select></div>"
    content += "<div class='col-md-4 mb-2'> <button class='btn btn-lg btn-block btn-primary' type='submit'> Afficher l'ecg </button></div></form>"

    server.send_response(200)
    server.send_header("Content-type", "text/html")
    server.end_headers()
    head = get_header()
    body = get_body(content)
    server.wfile.write(
        bytes(f"<html>{head} {body}</html>", "utf-8"))
