from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import view_index, view_patient, view_static

hostname = "localhost"
port = 8080


class ECGServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        qs = parse_qs(url.query)
        if self.path.startswith('/static/'):
            view_static(self)
        elif qs.get('patientid') and len(qs.get('patientid')) > 0:
            view_patient(self)
        else:
            view_index(self)


if __name__ == "__main__":
    webServer = HTTPServer((hostname, port), ECGServer)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
