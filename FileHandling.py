# file objects
# import os
# with open('test.txt','r') as rf:
# 	with open('test_copy.txt','w') as wf:
# 		for line in rf:
# 			wf.write(line)

	

# #print(f.closed)
# print(os.getcwd())

# for f in os.listdir():
# 	#print(f)
# 	filename, fileext = os.path.splitext(f)
# 	#print(filename, fileext)
# 	l_filename = filename.lower()

# 	#print(type(filename))
# 	#print(dir(str))
# 	new_name = f'{l_filename}{fileext}'
# 	os.rename(f, new_name)

import random

# create a deck of 52 cards
deck = list(range(1,53))
#print(deck)

# now shuffle the deck
random.shuffle(deck)
print(deck)

# get a hand of 5 cards
hand = random.sample(deck, k=5)
print(hand)

value = random.randint(0,1)
print(value)

values = random.randint(0,6)
print(values)

color = ['red','black','green']
print(random.choice(color))
print(random.choices(color, k=5))

list_random = list(range(100,999))
print(random.choices(list_random, k=10))