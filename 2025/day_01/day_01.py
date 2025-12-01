import sys
sys.path.append('/mnt/c/Users/gebra/work/adventofcode/2025')
from aoc_base import BaseDay
import math

class Day01(BaseDay):
    def __init__(self, dial_start: int = None, year: int = None, day: int = None,
                 script_file: str = None, **kwargs):
        super().__init__(year=year, day=day, script_file=script_file, **kwargs)
        self.dial_start = int(dial_start)


    def part1(self, data):
        dial = self.dial_start
        zeros_cnt = 0
        for line in data:
            direction = line[0]
            turns = int(line[1:])

            if direction == "L":
                turns *= -1
            dial += turns

            if dial % 100 == 0:
                zeros_cnt += 1

        return zeros_cnt


    def part2(self, data):
        dial = self.dial_start
        zeros_cnt = 0
        for line in data:
            direction = line[0]
            turns = int(line[1:])

            if direction == "L":
                turns *= -1
            prev = dial
            new = prev + turns

            if new >= prev:
                crossings = math.floor(new / 100) - math.floor(prev / 100)
            else:
                crossings = math.ceil(prev / 100) - math.ceil(new / 100)

            zeros_cnt += crossings
            dial = new
        return zeros_cnt


if __name__ == '__main__':
    Day01(dial_start=50, year=2025, day=1, script_file=__file__).run(suppress_timings = True)
