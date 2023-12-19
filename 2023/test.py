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
class Parts:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.accepted = None  # Initially, the acceptance status is set to None

    def set_accepted(self, status):
        if status in ['accepted', 'rejected']:
            self.accepted = status
        else:
            print("Invalid status. Please provide 'accepted' or 'rejected'.")

    def display_info(self):
        print(f"Attribute1: {self.x}")
        print(f"Attribute2: {self.m}")
        print(f"Attribute3: {self.a}")
        print(f"Attribute4: {self.s}")
        print(f"Accepted Status: {self.accepted}")