"""
Small helper module for Advent of Code day scripts.

Provides BaseDay which standardises input loading (relative to the script file),
common parsing helpers (ints, grids), timing and a simple run() method that
prints part outputs. Day scripts should import BaseDay and subclass it,
overriding part1() and part2().

Usage example in a day script (2025/day_01/day_01.py):

    from aoc_base import BaseDay

    class Day01(BaseDay):
        def part1(self, data):
            # data is the list of lines by default
            return len(data)

        def part2(self, data):
            return 0

    if __name__ == '__main__':
        Day01(year=2025, day=1, script_file=__file__).run()

The BaseDay constructor requires the script file path (pass __file__) so
that input files can be found reliably even when the script is invoked from
another current working directory.
"""
from __future__ import annotations

import os
import time
import re
from typing import List, Optional, Any


class BaseDay:
    """Base class for AoC day scripts.

    Parameters
    - year, day: integers identifying the puzzle
    - script_file: path to the day script (pass __file__ usually)
    - input_name: filename inside the day folder (default 'input.txt')
    - input_lines: optional pre-loaded lines (bypass file loading)
    """

    def __init__(self, year: int, day: int, script_file: Optional[str] = None,
                 input_name: str = 'input.txt', input_lines: Optional[List[str]] = None):
        self.year = int(year)
        self.day = int(day)
        self.input_name = input_name
        self.script_file = script_file
        self._input_lines = input_lines

        if script_file is not None:
            self.script_dir = os.path.dirname(os.path.abspath(script_file))
        else:
            # fallback to cwd
            self.script_dir = os.getcwd()

    @property
    def input_path(self) -> str:
        return os.path.join(self.script_dir, self.input_name)

    def read_lines(self, strip_newline: bool = True) -> List[str]:
        if self._input_lines is not None:
            return list(self._input_lines)

        with open(self.input_path, 'r', encoding='utf-8') as f:
            if strip_newline:
                return [line.rstrip('\n') for line in f]
            else:
                return [line for line in f]

    def read_text(self) -> str:
        if self._input_lines is not None:
            return '\n'.join(self._input_lines)
        with open(self.input_path, 'r', encoding='utf-8') as f:
            return f.read()

    def ints_in_line(self, line: str) -> List[int]:
        """Return all integers found in a line using regex (robust)."""
        return [int(x) for x in re.findall(r'-?\d+', line)]

    def read_all_ints(self) -> List[int]:
        """Return all integers appearing anywhere in the input file."""
        text = self.read_text()
        return [int(x) for x in re.findall(r'-?\d+', text)]

    def read_grid_chars(self) -> List[List[str]]:
        return [list(line) for line in self.read_lines()]

    def read_grid_ints(self) -> List[List[int]]:
        return [[int(c) for c in line] for line in self.read_lines()]

    # Convenience wrapper: subclasses override these
    def part1(self, data: Any) -> Any:
        raise NotImplementedError()

    def part2(self, data: Any) -> Any:
        raise NotImplementedError()

    def run(self, data: Optional[Any] = None, suppress_timings: bool = False) -> None:
        """Run parts and print results with optional timings.

        By default `data` is the list of input lines (stripped).

        Parameters
        - data: optional pre-parsed data to pass to part1/part2
        - suppress_timings: if True, the timing line will not be printed
          (useful when a caller/runner expects only the two result lines).
        """
        if data is None:
            data = self.read_lines()

        t0 = time.perf_counter()
        try:
            p1 = self.part1(data)
        except Exception as e:
            print(f'Error running part1: {e}')
            raise
        t1 = time.perf_counter()

        try:
            p2 = self.part2(data)
        except Exception as e:
            print(f'Error running part2: {e}')
            raise
        t2 = time.perf_counter()

        print(p1)
        print(p2)
        if not suppress_timings:
            print(f'# timings: p1={t1-t0:.4f}s p2={t2-t1:.4f}s')


if __name__ == '__main__':
    # quick smoke test when running this helper directly
    print('aoc_base module - not intended to be run directly')
