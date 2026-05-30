class Emploee:
    def __init__(self):
        print("Employee Hired")
    def __del__(self):
        print("Employee Fired")
def cobj():
    print("making object")
    obj = Emploee()
    print("function end")
    return obj

print("Create object function")
obj=cobj()
print("program end")