class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("invalid number of pins")
        if self._is_complete():
            raise IndexError("cannot roll after game is over")
        self.rolls.append(pins)
        self._validate_last_frame()

    def score(self):
        if not self._is_complete():
            raise IndexError("game is not complete")
        total = 0
        i = 0
        for _ in range(10):
            if self.rolls[i] == 10:
                total += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                i += 1
            elif self.rolls[i] + self.rolls[i + 1] == 10:
                total += 10 + self.rolls[i + 2]
                i += 2
            else:
                total += self.rolls[i] + self.rolls[i + 1]
                i += 2
        return total

    def _frames(self):
        """Return list of frames (each a list of rolls) for the first 10 frames,
        plus count of rolls consumed. Returns None if incomplete."""
        i = 0
        frames = []
        rolls = self.rolls
        for f in range(10):
            if i >= len(rolls):
                return None
            if rolls[i] == 10:
                frames.append([rolls[i]])
                i += 1
            else:
                if i + 1 >= len(rolls):
                    return None
                frames.append([rolls[i], rolls[i + 1]])
                i += 2
        return frames, i

    def _is_complete(self):
        res = self._frames()
        if res is None:
            return False
        frames, i = res
        last = frames[9]
        rolls = self.rolls
        if last[0] == 10:  # strike in 10th: need 2 fill balls
            return len(rolls) >= i + 2
        if sum(last) == 10:  # spare in 10th: need 1 fill ball
            return len(rolls) >= i + 1
        return len(rolls) >= i

    def _validate_last_frame(self):
        # Validate that no frame's two throws exceed 10 (except with fill balls)
        rolls = self.rolls
        i = 0
        frame = 0
        while frame < 10 and i < len(rolls):
            if rolls[i] == 10:
                i += 1
            elif i + 1 < len(rolls):
                if rolls[i] + rolls[i + 1] > 10:
                    raise ValueError("two rolls in a frame cannot exceed 10")
                i += 2
            else:
                break
            frame += 1
        # Validate fill balls in the 10th frame
        if frame == 10 and i < len(rolls):
            fills = rolls[i:]
            # If first fill is not a strike and there are 2 fills whose sum > 10, only valid if first is strike
            if len(fills) == 2 and fills[0] != 10 and fills[0] + fills[1] > 10:
                raise ValueError("invalid fill balls")
