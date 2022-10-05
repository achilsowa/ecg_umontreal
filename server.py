from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import view_index, view_patient, view_static
import config


"""
Just a simple web server used to do 3 things
1. Handle patient page
2. Handle static files (mainly images)
3. Show home page
"""


class ECGServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        qs = parse_qs(url.query)
        if self.path.startswith(f"/{config.STATIC_DIR}/"):
            view_static(self)
        elif qs.get("patientid") and len(qs.get("patientid")) > 0:
            view_patient(self)
        else:
            view_index(self)


if __name__ == "__main__":
    webServer = HTTPServer((config.HOST, config.PORT), ECGServer)
    print("Server started http://%s:%s" % (config.HOST, config.PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
