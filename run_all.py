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
    p.add_argument('-d', '--day', type=int, default=1,
                   help='select the day to run, options from 1 to 25 (default: %(default)s)',
                   action=StoreProvidedValue)
    p.add_argument('-y', '--year', type=int, choices=[int(d) for d in os.listdir()
                   if os.path.isdir(os.path.join(os.getcwd(), d)) and not d.startswith('.')],
                   default=max([int(d) for d in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), d))
                                and not d.startswith('.') and d.isdigit()]),
                   help='select the year to run (default: %(default)s)')
    p.add_argument('-a', '--all', action='store_true',
                   help='run all days available')

    return p.parse_args()


def parse_result(result, day, year):
    results = [[int(item) for item in r.split(',')] for r in open(str(year) + '/results.txt').read().splitlines()]
    if result.returncode == 0 and result.stdout != '':
        if (results[day-1][0] == int(result.stdout.split()[0]) and
                results[day-1][1] == int(result.stdout.split()[1])):
            print(f'\t[Passed] results: {results[day-1][0]}, {results[day-1][1]}')
        else:
            print(f'\t[P1] expected output:\t{results[day-1][0]}')
            print(f'\t[P1] calculated output:\t{result.stdout.split()[0]}')
            print(f'\t[P2] expected output:\t{results[day-1][1]}')
            print(f'\t[P2] calculated output:\t{result.stdout.split()[1]}')
    else:
        print(f'\tError running day {day} in {year}. Exit code:', result.returncode)
        print('\tError output:', result.stderr)
        print('\tScript output:', result.stdout)


def execute_scripts(args):
    if args.all:
        years = [y for y in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), y)) and not y.startswith('.')]
        for year in years:
            days = [d for d in os.listdir(year) if os.path.isdir(os.path.join(os.getcwd(), year, d))
                    and d.startswith('day')]
            for day in days:
                print(f"Running {day} from year {year}...")
                result = subprocess.run(['python', os.path.join(os.getcwd(), year, day, day + '.py')],
                                        capture_output=True, text=True,
                                        cwd=os.path.join(os.getcwd(), year, day))
                parse_result(result, int(re.findall(r'\d+', day)[0]), int(year))
    else:
        if hasattr(args, 'day_provided') and args.day_provided:
            day = f'day_{args.day:02}'
            print(f"Running {day} from year {args.year}...")
            result = subprocess.run(['python', os.path.join(os.getcwd(), str(args.year), day, day + '.py')],
                                    capture_output=True, text=True,
                                    cwd=os.path.join(os.getcwd(), str(args.year), day))
            parse_result(result, int(re.findall(r'\d+', day)[0]), int(args.year))
        else:
            days = [d for d in os.listdir(str(args.year)) if os.path.isdir(os.path.join(os.getcwd(), str(args.year), d))
                    and d.startswith('day')]
            for day in days:
                print(f"Running {day} from year {args.year}...")
                result = subprocess.run(['python', os.path.join(os.getcwd(), str(args.year), day, day + '.py')],
                                        capture_output=True, text=True,
                                        cwd=os.path.join(os.getcwd(), str(args.year), day))
                parse_result(result, int(re.findall(r'\d+', day)[0]), int(args.year))


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
