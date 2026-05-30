class Mammal:
    def __init__(self, warm_blooded):
        self.warm_blooded = warm_blooded
    def y(self):
        print("This animal is warm blooded")
class dog(Mammal):
    def __init__(self, warm_blooded, four_legs, fast, furry):
        self.four_legs = four_legs
        self.fast = fast
        self.furry = furry
        super().__init__(warm_blooded) 
    def a(self):
        print("This mammal is very fast")
    def b(self):
        print("This mammal is furry")
    def c(self):
        print("This mammal has four legs")
    def d(self):
        print("This mammal is a dog")

obj = dog(True, True, True, True)

obj.y()
obj.a()
obj.b()
obj.c()
obj.d()