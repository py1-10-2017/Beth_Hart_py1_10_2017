class Product(object):
    def __init__(self,price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        
    def sell(self):
        self.status = "sold"
        return self
        
    def add_tax(self, rate):
        total = self.price * (1 + rate)
        print "Total with Tax: " + str(total)
        return self

    
    def returned(self, reason):
        if reason == "defective":
            self.price = 0
            self.status = "defective"
        elif reason == "new":
            self.status = "for sale"
        elif reason == "open":
            self.price = self.price*.80
            self.status = "used"
        return self
    
    def display_all(self):
        print "price: $" + str(self.price)
        print "name: " + self.name
        print "weight: " + str(self.weight)
        print "brand: " + self.brand
        print "status: " + self.status
        return self

product1 = Product(4.50, "phone_cover", .12, "Tech Toys")
product2 = Product(499.99, "laptop", 15.2, "Fenceway")
product3 = Product(110.50, "wireless router", 6.75, "Boggle")
product4 = Product(4.50, "keyboard", 4.62, "Magitech")


product4.add_tax(.075).sell().display_all()
product4.returned("defective").display_all()
