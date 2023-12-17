import numpy as np

def checksym(xx: np.ndarray, smudgefix=False, debug=False) -> int:
    ln = xx.shape[0] - 1
    if debug:
        print(xx, ln)
    for row in range(1, ln + 1):
        if debug:
            print(f"{row = }")
        if 2 * row > ln:
            xxx = xx[ln - (ln - row) * 2 - 1 :]
        else:
            xxx = xx[: 2 * row]
        dif = xxx - np.flip(xxx, axis=0)
        if debug:
            print("xxx=")
            print(xxx)
            print("dif=")
            print(dif)
        if np.sum(dif == 1) == 1 and smudgefix:
            return row
        if not dif.any() and not smudgefix:
            return row
    return 0


def doit(smudgefix: bool, debug=False):
    lines = open('inputs/day_13_input.txt').read()
    fields = lines.split("\n\n")
    total = 0

    for field in fields:
        xx = np.array([[1 if char == "#" else 0 for char in line] for line in field.splitlines()])
        if debug:
            print(f"{checksym(xx, smudgefix)=} {checksym(xx.T, smudgefix)=}")

        total += 100 * checksym(xx, smudgefix)
        total += checksym(xx.T, smudgefix)

    return total


print(doit(False))
print(doit(True))