class store:
    def __init__(self):
        self.price = 1200
    def sell(self):
        print("The current price is", self.price)
    def updating(self, hello):
        self.price = hello

s = store()
s.sell()
s.updating(1000)
s.sell()
s.updating(1400)
s.sell()