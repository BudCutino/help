from http.server import BaseHTTPRequestHandler
import json
from fn import b
class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {"hello": b()}
    
        self.wfile.write(json.dumps(response).encode("utf-8"))

        return