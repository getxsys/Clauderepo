#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve index.html for root
        if self.path == '/':
            self.path = '/index.html'

        # Check if file exists
        file_path = os.path.join(os.getcwd(), self.path.lstrip('/'))
        if os.path.exists(file_path):
            # Serve the file
            super().do_GET()
        else:
            # Return 404 with error message
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 - File Not Found</h1>')
            self.wfile.write(b'<p>The requested file does not exist.</p>')
            self.wfile.write(b'<h2>Available files:</h2>')

            # List available files
            for filename in os.listdir('.'):
                if os.path.isfile(filename):
                    self.wfile.write(f'<a href="/{filename}">{filename}</a><br>'.encode())

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            print(f"Serving at http://localhost:{PORT}")
            print("Available files:")
            for filename in os.listdir('.'):
                if os.path.isfile(filename):
                    print(f"  {filename}")
            print("\nPress Ctrl+C to stop the server")
            httpd.serve_forever()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)