class PongSimulator:
    def __init__(self, lane_width=40, frames=20, ball="o", wall="|"):
        self.lane_width = max(4, min(lane_width, 120))
        self.frames = max(1, min(frames, 200))
        self.ball = ball
        self.wall = wall
        self.bounces = 0

    def run(self):
        pos = 0
        direction = 1
        rows = []
        for _ in range(self.frames):
            lane = [" "] * self.lane_width
            lane[pos] = self.ball
            rows.append(self.wall + "".join(lane) + self.wall)
            pos += direction
            if pos <= 0 or pos >= self.lane_width - 1:
                direction = -direction
                self.bounces += 1
                pos = max(0, min(pos, self.lane_width - 1))
        return rows