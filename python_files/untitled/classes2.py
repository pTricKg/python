#class ClassName(object):
    # class statements go here

class Car(object):
    condition = "new"
    def __init__(self,model,color,mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."

    def drive_car(self):
        self.condition = "used"

    
#newObject = ClassName()
my_car = Car("DeLorean", "silver", 88)

    

##print my_car.condition
##print my_car.model
##print my_car.color
##print my_car.mpg

# using display_car method to return same as above
print (my_car.display_car())

print ("My car is " + my_car.condition)
my_car.drive_car()
print ("I drove my car making it a " + my_car.condition + " car!")

#newObject = ClassName()

# Parents and Children
##class ChildClass(ParentClass):
##    # new variables and functions go here
class ElectricCar(Car):
    def __init__(self, model, color, mpg,battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"

my_car2 = ElectricCar("VW","green", 65, "molten salt")

print (my_car2.battery_type)

## using representation
class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return '(%d, %d, %d)' % (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)

print my_point
