from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ready")


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8041), Handler).serve_forever()
