from http.server import HTTPServer, BaseHTTPRequestHandler

import os

from plot import plot_it
from freestyleparser import get_dates, get_data
import sys

FMT = """<html>
<head><meta charset="utf-8" /></head>
<body>
{}
</body>
</html>
"""


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/":
            dates = get_dates(file)[::-1]

            body = "<h1>Libre Line Charts</h1><ul>{}</ul>".format(
                "".join(('<li><a href="/{0}">{0}</a></li>'.format(d) for d in dates))
            )

            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(FMT.format(body), "utf-8"))

        elif self.path.startswith("/20"):
            data = get_data(file, self.path[1:])

            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(FMT.format(plot_it(data)), "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(FMT.format("oops"), "utf-8"))


if __name__ == "__main__":

    # <file> [<port>]

    if len(sys.argv) < 2:
        print("No arguments. Please see the README.", file=sys.stderr)
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.isfile(file):
        print("File {} does not exist.".format(file), file=sys.stderr)
        sys.exit(1)

    port = 8000
    if len(sys.argv) >= 3:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Incorrect port number.", file=sys.stderr)
            sys.exit(1)

    httpd = HTTPServer(("localhost", port), RequestHandler)
    print("Data file: {}\nServing at port {}".format(file, port))
    httpd.serve_forever()
