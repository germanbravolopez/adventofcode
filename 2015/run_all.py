import subprocess

advent_days = [f'{day:02}' for day in range(1, 2)]

results = [[74, 1795],
           [1586300, 3737498],
        ]

for day in advent_days:
    script_path = f'day_{day}.py'
    result = subprocess.run(['python', script_path], capture_output=True, text=True)

    if result.returncode == 0 and result.stdout != '':
        if results[int(day)-1][0] == int(result.stdout.split()[0]) and results[int(day)-1][1] == int(result.stdout.split()[1]):
            print(f"Day {day} is passing...")
        else:
            print(f"Day {day}:")
            print(f"[P1] expected output:\t{results[int(day)-1][0]}")
            print(f"[P1] calculated output:\t{result.stdout.split()[0]}")
            print(f"[P2] expected output:\t{results[int(day)-1][1]}")
            print(f"[P2] calculated output:\t{result.stdout.split()[1]}")
    else:
        print(f"Error running {script_path}. Exit code:", result.returncode)
        print("Error output:", result.stderr)
        print("Script output:", result.stdout)