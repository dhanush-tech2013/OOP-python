class lowercase:
    def __init__(self):
        self.string1=""
    def inputmethod(self):
        self.string1 = input("Enter a string: ")
    def printing(self):
        print(self.string1.lower())

string1 = lowercase()
string1.inputmethod()
string1.printing()