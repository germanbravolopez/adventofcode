import subprocess, os, sys

if len(sys.argv) == 1:
    advent_days = [f'{day:02}' for day in range(1, int(sorted(os.listdir('inputs'))[-1][4:6]) + 1)]
elif len(sys.argv) == 2:
    advent_days=[f'{int(sys.argv[1]):02}']
else:
    print('Only 1 argument supported, it must specify the day to run...')
    sys.exit()

results = [[int(item) for item in r.split(',')] for r in open('results.txt').read().splitlines()]
if len(results) != len(advent_days):
    print('Number of results and inputs files are not matching')
    sys.exit()

for day in advent_days:
    script_path = f'day_{day}.py'
    print(f'Running day {day}...')
    result = subprocess.run(['python', script_path], capture_output=True, text=True)

    if result.returncode == 0 and result.stdout != '':
        if results[int(day)-1][0] == int(result.stdout.split()[0]) and results[int(day)-1][1] == int(result.stdout.split()[1]):
            print(f'\t[Passed] results: {results[int(day)-1][0]}, {results[int(day)-1][1]}')
        else:
            print(f'\t[P1] expected output:\t{results[int(day)-1][0]}')
            print(f'\t[P1] calculated output:\t{result.stdout.split()[0]}')
            print(f'\t[P2] expected output:\t{results[int(day)-1][1]}')
            print(f'\t[P2] calculated output:\t{result.stdout.split()[1]}')
    else:
        print(f'\tError running {script_path}. Exit code:', result.returncode)
        print('\tError output:', result.stderr)
        print('\tScript output:', result.stdout)