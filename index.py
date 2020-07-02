from http.server import BaseHTTPRequestHandler
import json
from fn import b

class handler(BaseHTTPRequestHandler):

    message = str(b())
    
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=UTF-8")
        # self.send_header("Content-type", "application/json")
        self.end_headers()
    
        self.wfile.write(self.message.encode("utf-8"))

        return