class dad:
    def __init__(self, eyes, nature):
        self.eyes= eyes
        self.nature = nature
    def display(self):
        print("Your eye color is: ", self.eyes)
        print("Your nature is: ", self.nature)

class son(dad):
    def __init__(self, name, age, eyes, nature):
        self.name = name
        self.age = age
        super().__init__(eyes, nature)

obj = son("abc", 9, "blue", "agressive")
obj.display()