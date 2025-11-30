import sys
sys.path.append(os.path.relpath("../../2025")

from aoc_base import BaseDay

class Day01(BaseDay):
    def part1(self, data):
        return len(data)

    def part2(self, data):
        return 0

if __name__ == '__main__':
    Day01(year=2025, day=1, script_file=__file__).run(suppress_timings = True)