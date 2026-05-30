class Person:
    def __init__(self, name, id):
        self.id = id
        self.name = name
    def display(self):
        print("Name is"+self.name)
        print("Id is"+self.id)

class child(Person):
    def __init__(self,name, id, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, id)

obj = child("ab", "141424", "$2412", "Tower")
obj.display()