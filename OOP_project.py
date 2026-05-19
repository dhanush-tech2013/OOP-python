class vehicle:
    def __init__(self, miles, speed):
        self.miles = miles
        self.speed = speed
BMW = vehicle(12, 100)
Toyota = vehicle(100,12)

print(Toyota.miles, Toyota.speed)
print(BMW.miles, BMW.speed)
