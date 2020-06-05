# Example 1 -- empty __init__.py

import animals1

animals1.dog.speak()
dir(animals1)

from animals1 import dog
dog.speak()
dir(animals1)
animals1.dog.speak()

animals1.cat.speak()
import animals1.cat
animals1.cat.speak()
cat.speak()

# What do you get if you want behavior like
import os
os.path


# Example 2 -- non-empty __init__.py

import animals2
animals2.dog.speak()
animals2.cat.speak()
animals2.goose.speak()

# This also gets you
from animals2 import *
goose.speak()


# Example 3 -- importing a package just sources __init__.py

import animals3

animals3.squirrel.speak()
animals3.cat.speak()
animals3.cat()


# Example 4 -- defining __all__ in __init__.py

import animals4
# does not work:
animals4.goose.speak()

# Sources all the submodules:
from animals4 import *


# Example 5 -- no __init__.py

# Works just like Example 1
import animals5.dog

animals5.dog.speak()
