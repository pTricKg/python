### Classes
##class Fruit(object): # what class inherits is in parenthesis
##	"""A class that makes various tasty fruits."""
##	def __init__(self, name, color, flavor, poisonous): # used to initialize objects
##		self.name = name # these are objects being created by class
##		self.color = color
##		self.flavor = flavor
##		self.poisonous = poisonous
##	
##	def description(self):
##		print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)
##		
##	def is_edible(self):
##		if not self.poisonous:
##			print "Yep! I'm edible."
##		else:
##			print "Don't eat me! I am super poisonous."
##
##lemon = Fruit("lemon", "yellow", "sour", False)
##
##lemon.description()
##lemon.is_edible()
##
### creating Animal Class
##class Animal(object):
##    is_alive = True # member variable
##    def __init__(self,name, age, is_hungry): # functions is classes
##                                              # are 'methods'
##        self.name = name
##        self.age = age
##        self.is_hungry = is_hungry
##
##    # creating another method
##    def description(self):
##	    print self.name
##	    print self.age
##	    
##hippo = Animal("Hip", 24)
##
##hippo.description()
##
### Note that self is only used in the __init__()
### function definition; we don't need to pass it
### to our instance objects.
##
##zebra = Animal("Jeffrey", 2, True) # creating instances of Animal Class
##giraffe = Animal("Bruce", 1, False)
##panda = Animal("Chad", 7, True)
##
##print zebra.name, zebra.age, zebra.is_hungry, is_alive
##print giraffe.name, giraffe.age, giraffe.is_hungry, is_alive
##print panda.name, panda.age, panda.is_hungry, is_alive
##        
##zebra = Animal("Jeffrey") # creating instance of Animal Class
##
##print zebra.name

''' Shopping Cart '''
# creating shopping cart program
##class ShoppingCart(object):
##    """Creates shopping cart objects
##    for users of our fine website."""
##    items_in_cart = {}
##    def __init__(self, customer_name):
##        self.customer_name = customer_name
##		
##    def add_item(self, product, price):
##        """Add product to the cart."""
##        if not product in self.items_in_cart:
##            self.items_in_cart[product] = price
##            print (product + " added.")
##        else:
##            print (product + " is already in the cart.")
##		
##    def remove_item(self, product):
##        """Remove product from the cart."""
##        if product in self.items_in_cart:
##            del self.items_in_cart[product]
##            print (product + " removed.")
##        else:
##            print (product + " is not in the cart.")
##
##my_cart = ShoppingCart("Mine") # creating instance for my cart within ShoppingCart
##my_cart.add_item("Computer", 500)

### getting on with inheritance
##class Customer(object):
##    """Produces objects that represent customers."""
##    def __init__(self, customer_id):
##        self.customer_id = customer_id
##	
##    def display_cart(self):
##        print "I'm a string that stands in for the contents of your shopping cart!"
##
##class ReturningCustomer(Customer): # inherits from Customer Class
##    """For customers of the repeat variety."""
##    def display_order_history(self):
##        print "I'm a string that stands in for your order history!"
##
##monty_python = ReturningCustomer("ID: 12345")
##monty_python.display_cart()
##monty_python.display_order_history()

# making shapes with Class
##class Shape(object):
##    """Makes shapes!"""
##    def __init__(self, number_of_sides):
##        self.number_of_sides = number_of_sides
##
### Add your Triangle class below!
##class Triangle(Shape):
##    def __init__(self, side1, side2, side3):
##        self.side1 = side1
##        self.side2 = side2
##        self.side3 = side3

# employees
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
	
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def __init__(self): # the following will override wage calc from parent
        def calculate_wage(self, hours):
            self.hours = hours
            return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(self, hours)
                
milton = PartTimeEmployee()
print (milton.full_time_wage)

''' syntax for accessing attributes and methods from parent
class DerivedClass(Base):
   def some_method(self):
       super(DerivedClass, self).meth()'''

# more Triangles
class Triangle(object):
    number_of_sides = 3
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def check_angles(Triangle):
        if self.side1 + self.side2 + self.side3 == 180:
            return True
        else:
            return False

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = angle
        self.angle2 = angle
        self.angle3 = angle
            
            
my_triangle = Triangle(30,30,30)

print my_triangle.number_of_sides
print my_triangle.check_angles
