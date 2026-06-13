# ── DAY 9: Inheritance and super() ──

# ── PARENT CLASS — the base ──
class Animal:

    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

    def describe(self):
        print(f"I am {self.name}")


# ── CHILD CLASSES — inherit from Animal ──
class Dog(Animal):           # Dog inherits Animal
    def fetch(self):         # Dog has its OWN method too
        print(f"{self.name} fetches the ball!")

class Cat(Animal):           # Cat inherits Animal
    def purr(self):
        print(f"{self.name} purrs...")


# Create objects
dog = Dog("Rex", "Woof")
cat = Cat("Whiskers", "Meow")

# Inherited methods work automatically
dog.speak()      # Rex says Woof    — inherited from Animal
dog.describe()   # I am Rex         — inherited from Animal
dog.fetch()      # Rex fetches...   — Dog's own method

cat.speak()      # Whiskers says Meow
cat.purr()       # Whiskers purrs...

# Check inheritance
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True — dog IS an Animal too!