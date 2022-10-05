import os

"""
Simple static access file manager. Can handle only .css and .png files
"""


def view(server):
    filename = os.getcwd() + server.path
    server.send_response(200)

    if filename[-4:] == '.css':
        server.send_header('Content-type', 'text/css')
    elif filename[-4:] == '.png':
        server.send_header('Content-type', 'image/png')
    else:
        server.send_header('Content-type', 'text/html')

    server.end_headers()

    with open(filename, 'rb') as fh:
        html = fh.read()
        server.wfile.write(html)
