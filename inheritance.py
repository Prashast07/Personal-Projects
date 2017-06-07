class Vehicle:
    def general_usage(self):
        print("general use: transporation")

class Car(Vehicle):
    def __init__(self,wheels,roof):
        print("I'm car")
        self.wheels = wheels
        self.has_roof = roof
    def print_properties(self):
        print self.wheels
        print self.has_roof

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")

c = Car(4,"No")
c.print_properties()
c.specific_usage()
#m = MotorCycle()

#print(issubclass(Car,MotorCycle))