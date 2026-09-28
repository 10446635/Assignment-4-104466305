import socket
from datetime import datetime, timezone

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "SWE40006 Task 4.2\n"
        "104466305 Callum Gesthuizen\n"
        f"container: {socket.gethostname()}\n"
        f"time: {datetime.now(timezone.utc).isoformat()}\n",
        200,
        {"Content-Type": "text/plain"},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)