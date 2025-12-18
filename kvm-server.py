from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from urllib.parse import urlparse

HOST = ""
PORT = 5000

class KvmRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == "/1":
            self.send_code("866b02fd")
        elif parsed_path.path == "/2":
            self.send_code("866b05fa")
        elif parsed_path.path == "/3":
            self.send_code("866b08f7")
        elif parsed_path.path == "/4":
            self.send_code("866b1be4")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def send_code(self, code):
        os.system("ir-ctl -S nec:0x" + code)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())

if __name__ == "__main__":
    print(f"Starting server at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), KvmRequestHandler)
    server.serve_forever()
