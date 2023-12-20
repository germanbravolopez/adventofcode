import re


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


data = open('input.txt').read().strip().split('\n\n')

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
print(-1)
