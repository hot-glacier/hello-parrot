import random

#this is an example

print('The parrot looks at you expectantly.\n')
a = input('You say, for some reason, to the parrot: \n')
x = random.randint(0,2)
sayings = ['Arrrr, ','Ahoy, ','Squaaack, ']
y = sayings[x]

print('\n' + "The parrot of wisdom says '" + y + a + "'")
