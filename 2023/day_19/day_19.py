import re

INPUT_FILE_PATH = 'input.txt'
START_WF = 'in'
ACCEPT = 'A'
REJECT = 'R'
GREATER = ">"
LESS = "<"


# MyParts format: each objet has attributes: {x, m, a, s, status}
class MyParts:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.status = None  # Initially, the acceptance status is set to None

    def __str__(self):
        return f"x: {self.x}, m: {self.m}, a: {self.a}, s: {self.s}, status: {self.status}"

    def set_status(self, status):
        if status in ['A', 'R']:
            self.status = status
        else:
            print("Invalid status. Please provide 'A' or 'R'.")


# Returns True if the part is compliant with the condition
def parse_condition(p, cond):
    match re.split(r'[<>]', cond)[0]:
        case 'x':
            if (('<' in cond and p.x < int(re.split(r'[<>]', cond)[1])) or
                    ('>' in cond and p.x > int(re.split(r'[<>]', cond)[1]))):
                return True
            else:
                return False
        case 'm':
            if (('<' in cond and p.m < int(re.split(r'[<>]', cond)[1])) or
                    ('>' in cond and p.m > int(re.split(r'[<>]', cond)[1]))):
                return True
            else:
                return False
        case 'a':
            if (('<' in cond and p.a < int(re.split(r'[<>]', cond)[1])) or
                    ('>' in cond and p.a > int(re.split(r'[<>]', cond)[1]))):
                return True
            else:
                return False
        case 's':
            if (('<' in cond and p.s < int(re.split(r'[<>]', cond)[1])) or
                    ('>' in cond and p.s > int(re.split(r'[<>]', cond)[1]))):
                return True
            else:
                return False


data = open(INPUT_FILE_PATH).read().strip().split('\n\n')

workflows_input = data[0].split('\n')
parts_input = data[1].split('\n')

# Organize workflows in dict: {'label': [[cond1:dest1], [cond2:dest2], [dest3]]}
workflows = dict()
for workflow in workflows_input:
    steps = []
    for step in workflow.split('{')[1].split(','):
        if ':' in step:
            steps.append([step.split(':')[0], step.split(':')[1]])
        else:
            steps.append([step[:-1]])
    workflows[workflow.split('{')[0]] = steps
# Organize parts in MyParts class
parts = []
for part in parts_input:
    parts.append(MyParts(int(re.findall(r'\d+', part.split(',')[0])[0]),
                         int(re.findall(r'\d+', part.split(',')[1])[0]),
                         int(re.findall(r'\d+', part.split(',')[2])[0]),
                         int(re.findall(r'\d+', part.split(',')[3])[0])))
# Set status for each part
for part in parts:
    current_step = 'in'
    while current_step not in ['A', 'R']:
        for step in workflows.get(current_step):
            if len(step) > 1:
                if parse_condition(part, step[0]):
                    current_step = step[1]
                    break
            else:
                current_step = step[0]
    part.set_status(current_step)
# Calculate all
print(sum(part.x + part.m + part.a + part.s for part in parts if part.status == 'A'))


# Part 2
def calculate_ranges_product(ranges):
    product = 1
    for start, end in ranges.values():
        product *= end - start + 1
    return product


def get_accepted_comb_number(ranges, wf_name):
    # BASE CASE (1)
    if wf_name == REJECT:
        return 0
    # BASE CASE (2)
    if wf_name == ACCEPT:
        return calculate_ranges_product(ranges)

    rules, default = WF[wf_name]  # rules: list of rules; default: default workflow name

    total = 0
    is_condition_impossible = False
    for var, symb, num, target in rules:
        start, end = ranges[var]
        # Calculate the range for the true and false condition
        if symb == LESS:
            rule_true_range = (start, num - 1)
            rule_false_range = (num, end)
        else:  # symb == GREATER:
            rule_true_range = (num + 1, end)
            rule_false_range = (start, num)

        if rule_true_range[0] <= rule_true_range[1]:
            ranges_copy = dict(ranges)
            ranges_copy[var] = rule_true_range
            total += get_accepted_comb_number(ranges_copy, target)

        if rule_false_range[0] <= rule_false_range[1]:
            ranges = dict(ranges)
            ranges[var] = rule_false_range
        else:
            # Impossible Condition
            is_condition_impossible = True
            break

    if not is_condition_impossible:
        total += get_accepted_comb_number(ranges, default)

    return total


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        file = f.read()

    wf_file, parts_file = file.split('\n\n')

    # Parts parsing
    parts = set()
    regex = re.compile('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
    for line in parts_file.split('\n'):
        match = re.fullmatch(regex, line)
        parts.add(tuple(map(int, match.groups())))

    # Workflow parsing
    workflows = dict()
    rule_regex = re.compile('([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)')
    for line in wf_file.split('\n'):
        # Name
        index_of_curly = line.index('{')
        name = line[:index_of_curly]
        # Default rule
        rest_line = line[index_of_curly + 1:len(line) - 1]
        default = rest_line.split(',')[-1]
        # Rules
        rules = []
        matches = re.findall(rule_regex, rest_line)
        for match in matches:
            rules.append((match[0], match[1], int(match[2]), match[3]))
        workflows[name] = (rules, default)

    return parts, workflows


# Solve it
_, WF = parse_input_file()
rages_dict_0 = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000)
}
print(get_accepted_comb_number(rages_dict_0, START_WF))
