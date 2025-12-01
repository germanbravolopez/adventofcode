import sys
sys.path.append(os.path.relpath("../../2025")

from aoc_base import BaseDay
import math

class Day01(BaseDay):
    def __init__(self, dial_start: int = None, year: int = None, day: int = None,
                 script_file: str = None, **kwargs):
        super().__init__(year=year, day=day, script_file=script_file, **kwargs)
        self.dial_start = int(dial_start)


    def count_zeros(self, data, p1: bool = True):
        dial = self.dial_start
        zeros_cnt = 0
        zeros_crossing_cnt = 0
        for line in data:
            direction = line[0]
            turns = int(line[1:])

            if direction == "L":
                turns *= -1

            prev = dial
            dial += turns

            # Part 1: count if we land on a zero
            if dial % 100 == 0:
                zeros_cnt += 1

            # Part 2: count how many zeros we crossed
            if dial >= prev:
                crossings = math.floor(dial / 100) - math.floor(prev / 100)
            else:
                crossings = math.ceil(prev / 100) - math.ceil(dial / 100)
            zeros_crossing_cnt += crossings

        return zeros_cnt if p1 else zeros_crossing_cnt


    def part1(self, data):
        return self.count_zeros(data)


    def part2(self, data):
        return self.count_zeros(data, p1=False)


if __name__ == '__main__':
    Day01(dial_start=50, year=2025, day=1, script_file=__file__).run(suppress_timings = True)
