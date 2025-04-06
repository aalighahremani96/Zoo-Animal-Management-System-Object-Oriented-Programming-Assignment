class Animal:
    zoo_name="asghars zoo"
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        print(f"this animal goes:{self.sound}")
    
    def info(self):
        print(f"{self.name} is a {self.species} and is {self.age} years old and makes a {self.sound} sound.")
    
    def __str__(self):
        r=f"{self.name} is a {self.species} and is {self.age} years old and makes a {self.sound}sound. (second way)"
        return r
###

lion=Animal("asghar", "cat", 5, "roar")
lion.info()
print(str(lion))

###
class bird(Animal):
    def __init__(self, span, name, species, age, sound):
        Animal.__init__(self, name, species, age, sound)
        self.span = span
    
    def make_sound(self):
        print(f"this bird goes: {self.sound} which is cool")
    
    def wing_span(self):
        print(f"this bird has a wing span of {self.span}")
    
    def info(self):
        print(f"{self.name} is a {self.species} and is {self.age} years old and makes a {self.sound} sound and has a wing span of {self.span} meters.")    

######

kalagh=bird(2, "black", "parande", "72", "Ghooghooli")
kalagh.info()



