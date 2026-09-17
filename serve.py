"""Local-only AFTERLIGHT launcher. Python 3.9+; no packages required."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys
import webbrowser

ROOT = Path(__file__).resolve().parent / "dist"
HOST, PORT = "127.0.0.1", 8767


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, ".mjs": "text/javascript", ".json": "application/json"}

    def list_directory(self, path):
        self.send_error(404, "Directory listing is disabled")

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()


def main():
    try:
        server = ThreadingHTTPServer((HOST, PORT), partial(Handler, directory=str(ROOT)))
    except OSError as error:
        print(f"Could not start http://{HOST}:{PORT}: {error}")
        print("Close another AFTERLIGHT launcher, then try again.")
        return 1
    print(f"AFTERLIGHT is ready: http://{HOST}:{PORT}")
    print("Keep this window open. Press Ctrl+C to stop.")
    if "--no-open" not in sys.argv:
        webbrowser.open(f"http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
