from lesson_package.tools import utils
# from lesson_package.talk import human
# from lesson_package.talk import animal
from lesson_package.talk import *

r = utils.say_twice('hello')
print(r)

r = human.sing()
print(r)

r = human.cry()
print(r)

print(animal.sing())
print(animal.cry())
