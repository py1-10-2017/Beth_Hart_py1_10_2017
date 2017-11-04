class Animal():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
        
    def run(self):
        self.health -= 5
        return self
        
    def display_health(self):
        print(self.name.title() + ' ' + str(self.health))
        return self
        
animal1 = Animal("bob", 100).walk().walk().run().display_health()
animal2 = Animal('sally', 150).display_health()

class Dog(Animal):
    def __init__(self, name, legs, health=150):
        super().__init__(name, health)
        self.legs = legs
    def pet(self):
        self.health += 5
        return self

animal3 = Dog('leo', 4).display_health()
animal3.walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name, health=170):
        super().__init__(name, health)
            
    def fly(self):
        self.health -= 10
        
    def display_health(self):
        Animal.display_health(self)
        print("I am a dragon")
        
animal4 = Dragon("pete")
animal4.display_health()


class Cow(Animal):
    def __init__(self, name, diet, health=50):
        super().__init__(name, health)
        self.diet = diet
    def display_health(self):
        Animal.display_health(self)
        print("i eat grass")
        return self

animal5= Cow('murphy','grass').display_health()

print(animal5.diet)