"""
Advent of code run_all.py script.
Copyright (c) 2023, German Bravo
"""

import sys
import os
import argparse
import subprocess
import re
import traceback


class StoreProvidedValue(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest + '_provided', True)
        setattr(namespace, self.dest, values)


def cmdline_args():
    # Make parser object
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('-d', '--day', type=int,
                   help='select which day to run, options from 1 to 25 (default: complete year)',
                   action=StoreProvidedValue)
    p.add_argument('-y', '--year', type=int, choices=[int(d) for d in os.listdir()
                   if os.path.isdir(os.path.join(os.getcwd(), d)) and not d.startswith('.') and d[0].isdigit()],
                   default=max([int(d) for d in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), d))
                                and not d.startswith('.') and d.isdigit()]),
                   help='select the year to run (default: %(default)s)')
    p.add_argument('-a', '--all', action='store_true',
                   help='run all days available')

    return p.parse_args()


def print_results(expected, calculated, part):
    print(f'\t[{part}] expected output:\t{expected}')
    print(f'\t[{part}] calculated output:\t{calculated}')


def parse_result(result, day, year):
    with open(f"{year}/results.txt") as file:
        results = [[int(item) for item in r.split(',')] for r in file.read().splitlines()]

    output_parts = result.stdout.split()

    if result.returncode == 0 and output_parts:
        if len(output_parts) in {1, 2} and all(part.isdigit() for part in output_parts):
            if len(output_parts) == 2:
                result_p1, result_p2 = (output_parts[0], output_parts[1])
            else:
                result_p1, result_p2 = (output_parts[0], None)

            if result_p2 is not None:
                if results[day - 1][0] == int(result_p1) and results[day - 1][1] == int(result_p2):
                    print(f'\t[Passed] results: {results[day - 1][0]}, {results[day - 1][1]}')
                else:
                    print_results(results[day - 1][0], result_p1, 'P1')
                    print_results(results[day - 1][1], result_p2, 'P2')
            else:
                if results[day - 1][0] == int(result_p1):
                    print(f'\t[Partially passed] result: {results[day - 1][0]}')
                    print(f'\tStill missing results for part 2...')
                else:
                    print_results(results[day - 1][0], result_p1, 'P1')
        else:
            print(f'\tPrint statement(s) from {year}/day_{day} cannot be parsed: "{output_parts[0]}"')
    else:
        print(f'\tError running day {day} in {year}. Exit code: {result.returncode}')
        print(f'\tError output:', result.stderr.split())
        print(f'\tScript output:', result.stdout.split())


def run_script(year, day):
    """Runs the specified script for the given year and day."""
    print(f"Running {day} from year {year}...")
    if not os.path.exists(os.path.join(os.getcwd(), year, day, day + '.py')):
        print(f"\tScript {day}.py not found in {year}/{day}/")
        return
    # use the same python interpreter that is running this script
    result = subprocess.run([sys.executable, os.path.join(os.getcwd(), year, day, day + '.py')],
                            capture_output=True, text=True, cwd=os.path.join(os.getcwd(), year, day))
    parse_result(result, int(re.findall(r'\d+', day)[0]), int(year))


def execute_scripts(args):
    if args.all:
        # Only consider directories whose names are numeric year values (e.g. '2015', '2024')
        years = sorted([y for y in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), y)) and y.isdigit()], key=int)
        for year in years:
            days = [d for d in os.listdir(year) if os.path.isdir(os.path.join(os.getcwd(), year, d))
                    and d.startswith('day')]
            for day in days:
                run_script(year, day)
    else:
        if hasattr(args, 'day_provided') and args.day_provided:
            day = f'day_{args.day:02}'
            run_script(str(args.year), day)
        else:
            days = [d for d in os.listdir(str(args.year)) if os.path.isdir(os.path.join(os.getcwd(), str(args.year), d))
                    and d.startswith('day')]
            for day in days:
                run_script(str(args.year), day)


if __name__ == '__main__':
    if sys.version_info < (3, 5, 0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    try:
        execute_scripts(cmdline_args())

    except Exception as e:
        if not isinstance(e, SystemExit):
            print(f"An exception occurred: {e}")
            traceback.print_exc()
