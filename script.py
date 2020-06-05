import os
os.path()


# Example 1 -- empty __init__.py

import animals1

animals1.dog.speak()
# dir(animals1)

# from animals1 import dog
# dog.speak()
# # dir(animals1)
# animals1.dog.speak()

animals1.cat.speak()
import animals1.cat
animals1.cat.speak()
cat.speak()


# Example 2 -- non-empty __init__.py

import animals2


# Example 3 -- importing a package just sources __init__.py

import animals3

animals3.dog.speak()
animals3.cat.speak()
animals3.goose.speak()

# This also gets you
from animals3 import *
goose.speak()


# Example 4 -- no __init__.py

# Works just like Example 1
import animals5.dog

animals5.dog.speak()
