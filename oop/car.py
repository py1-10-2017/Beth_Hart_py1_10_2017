class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12
        if self.price > 10000:
            self.tax = .15
    
    def display_all(self):
        print "price: $"+ str(self.price)
        print "speed: " + str(self.speed) + "mph"
        print "fuel: " + str(self.fuel)
        print "mileage: " + str(self.mileage)
        print "tax: " + str(self.tax)
        
car1 = Car(16000, 45, "Full", 85000).display_all()
car1 = Car(1000, 45, "3/4", 3450).display_all()
car1 = Car(8500, 45, "Half", 26200).display_all()
car1 = Car(5, 45, "Empty", 3).display_all()
car1 = Car(30000, 45, "Full", 5000).display_all()
        
