import os
import socket

from flask import Flask, render_template_string

from pong import PongSimulator

app = Flask(__name__)

#COOL NEW CHANGE

# Copypasta from assignment 2
LABEL = os.environ.get("DEPLOY_LABEL", "local-development")
LANE = int(os.environ.get("PONG_LANE_WIDTH", "40"))
FRAMES = int(os.environ.get("PONG_FRAMES", "20"))
BALL = os.environ.get("PONG_BALL_CHAR", "o")
WALL = os.environ.get("PONG_WALL_CHAR", "|")

PAGE = """<!doctype html>
<title>Pong Simulator</title>
<style>body{font-family:system-ui;margin:2rem}pre{line-height:1.1}</style>
<h1>Pong Simulator</h1>
<p>104466305 &mdash; SWE40006 Deployment Task 4</p>
<table>
<tr><td>Deployment label</td><td>{{ label }}</td></tr>
<tr><td>Container</td><td>{{ host }}</td></tr>
<tr><td>Lane width</td><td>{{ lane }}</td></tr>
<tr><td>Frames</td><td>{{ frames }}</td></tr>
<tr><td>Ball / wall</td><td>{{ ball }} / {{ wall }}</td></tr>
<tr><td>Bounces</td><td>{{ bounces }}</td></tr>
</table>
<pre>{{ rows }}</pre>
"""


@app.route("/")
def index():
    sim = PongSimulator(LANE, FRAMES, BALL, WALL)
    rows = sim.run()
    return render_template_string(
        PAGE, label=LABEL, host=socket.gethostname(), lane=LANE,
        frames=FRAMES, ball=BALL, wall=WALL, bounces=sim.bounces,
        rows="\n".join(rows),
    )


@app.route("/health")
def health():
    return {"status": "healthy", "container": socket.gethostname()}, 200