from http.server import BaseHTTPRequestHandler, HTTPServer
import mimetypes
import ssl
import sys

class ImageRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        
        self.send_header("Content-Type", self.server.image[0])
        self.end_headers()

        self.wfile.write(self.server.image[1])

if __name__ == "__main__":
    server = HTTPServer(("cdn.discordapp.com", 443), ImageRequestHandler)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    server.socket = context.wrap_socket(server.socket, server_side=True)

    with open(sys.argv[-1], "rb") as file:
        data = file.read()

    server.image = (mimetypes.guess_type(sys.argv[-1])[0], data)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()