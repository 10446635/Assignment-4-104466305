import argparse
import os
import sys
from datetime import datetime, timezone

from pong import PongSimulator


def main():
    parser = argparse.ArgumentParser(
        description="Renders a ping-pong simulation to stdout and to a file."
    )
    parser.add_argument("--lane-width", type=int,
                        default=int(os.environ.get("PONG_LANE_WIDTH", "40")))
    parser.add_argument("--frames", type=int,
                        default=int(os.environ.get("PONG_FRAMES", "20")))
    parser.add_argument("--ball", default=os.environ.get("PONG_BALL_CHAR", "o"))
    parser.add_argument("--wall", default=os.environ.get("PONG_WALL_CHAR", "|"))
    parser.add_argument("--out", default=os.environ.get("PONG_OUT", "/data"))
    args = parser.parse_args()

    sim = PongSimulator(args.lane_width, args.frames, args.ball, args.wall)
    rows = sim.run()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    path = os.path.join(args.out, f"pong-{stamp}.txt")

    try:
        with open(path, "w") as f:
            f.write("\n".join(rows) + "\n")
    except OSError as e:
        print(f"could not write {path}: {e}", file=sys.stderr)
        return 1

    for row in rows:
        print(row)
    print(f"frames={args.frames} lane={args.lane_width} bounces={sim.bounces}")
    print(f"written to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
