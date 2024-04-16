import http.server
import socketserver
import urllib.parse


def send_hello_response(handler):
    handler.send_response(200)
    handler.send_header("Content-type", "text/html")
    handler.end_headers()
    handler.wfile.write(bytes("Hello from Python server!", "utf-8"))


class HelloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == '/':
            send_hello_response(self)
        else:
            # Serve static files for other paths
            super().do_GET()


PORT = 8000

with socketserver.TCPServer(("", PORT), HelloHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
