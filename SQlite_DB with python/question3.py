class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def display_branches(self):
        print(f"Branches of {self.name}:")
        for branch in self.branches:
            print(branch)


my_bank = Bank("Chase")
my_bank.add_branch("New York")
my_bank.add_branch("Chicago")
my_bank.display_branches()
