import re

class MyParts:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.status = None # Initially, the acceptance status is set to None

    def __str__(self):
        return f"x: {self.x}, m: {self.m}, a: {self.a}, s: {self.s}, status: {self.status}"

    def set_status(self, status):
        if status in ['A', 'R']:
            self.status = status
        else:
            print("Invalid status. Please provide 'A' or 'R'.")


input = open('inputs/day_19_input.txt').read().strip().split('\n\n')

workflows_input = input[0].split('\n')
parts_input = input[1].split('\n')

# Organize workflows in dict
workflows = dict()
for workflow in workflows_input:
    steps = []
    for step in workflow.split('{')[1].split(','):
        if ':' in step:
            steps.append([step.split(':')[0], step.split(':')[1]])
        else:
            steps.append([step[:-1]])
    workflows[workflow.split('{')[0]] = steps
#print(workflows)

# Organize parts in a class
parts = []
for part in parts_input:
    parts.append(MyParts(int(re.findall(r'\d+', part.split(',')[0])[0]),
                         int(re.findall(r'\d+', part.split(',')[1])[0]),
                         int(re.findall(r'\d+', part.split(',')[2])[0]),
                         int(re.findall(r'\d+', part.split(',')[3])[0])))
#print(parts[0].x)

# Classify parts
def parse_condition(part, condition):
    match re.split(r'<|>', condition)[0]:
        case 'x':
            if (('<' in condition and part.x < int(re.split(r'<|>', condition)[1])) or
                ('>' in condition and part.x > int(re.split(r'<|>', condition)[1]))):
                return True
            else:
                return False
        case 'm':
            if (('<' in condition and part.m < int(re.split(r'<|>', condition)[1])) or
                ('>' in condition and part.m > int(re.split(r'<|>', condition)[1]))):
                return True
            else:
                return False
        case 'a':
            if (('<' in condition and part.a < int(re.split(r'<|>', condition)[1])) or
                ('>' in condition and part.a > int(re.split(r'<|>', condition)[1]))):
                return True
            else:
                return False
        case 's':
            if (('<' in condition and part.s < int(re.split(r'<|>', condition)[1])) or
                ('>' in condition and part.s > int(re.split(r'<|>', condition)[1]))):
                return True
            else:
                return False

for part in parts:
    current_step = 'in'
    while not current_step in ['A', 'R']:
        # First step is 'in'
        #print(current_step, workflows.get(current_step))
        for step in workflows.get(current_step):
            if len(step) > 1:
                #print(parse_condition(part, step[0]))
                if parse_condition(part, step[0]):
                    current_step = step[1]
                    break
            else:
                #print(step[0])
                current_step = step[0]
    part.set_status(current_step)

# Calculate all
print(sum(part.x + part.m + part.a + part.s for part in parts if part.status == 'A'))