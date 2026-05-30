class myclass:
    a = 12
    def private(self):
        print("Hello")
    def printing(self):
        print("The private number is:", myclass.a)

o = myclass()
o.private()
o.printing()