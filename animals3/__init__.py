from . import cat
from . import dog
from . import goose

cat = cat.speak
dog = dog.speak
goose = goose.speak

print("Hi, I'm __init__.py")

class Squirrel:
    def __init__(self):
        return
    
    def speak(self):
        print("...")

squirrel = Squirrel()

