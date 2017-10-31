class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "price is: ",self.price
        print "max speed is: ", self.max_speed
        print "total miles: ", self.miles
        return self
        
    def ride(self):
        print "riding..."
        self.miles = self.miles + 10
        return self
        
    def reverse(self):
        print "reversing..."
        self.miles = self.miles - 5
        return self

old_bike = Bike(100, 12)
new_bike = Bike(600, 18)
        
        
old_bike.ride().ride().ride().reverse().displayInfo()
new_bike.ride().ride().reverse().reverse().displayInfo()
