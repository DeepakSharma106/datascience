nums = [1,2,3,4,5,6,7,8,9]

my_nums = []

for n in nums:
	my_nums.append(n*n)

print(my_nums)

print('using list comprehension ',[n*n  for n in nums])

# using map

# map(anonymous function, list)
new_list  = map(lambda n: n*n, nums)

#get the even numbers
print([x for x in my_nums if x % 2 == 0])

li1 = []
for letter in 'abcd':
	for num in range(4):
		li1.append((letter, num))

print(li1)

print([(letter, num) for letter in 'abcd' for num in range(4)])
names = ['amit','sumit','kalu','ghoru']

marks = [44,67,89,22]

diction = {}
for name, mark in zip(names, marks):
	diction[name] = mark
print(diction)

print({name:marks for name, marks in zip(names, marks) if name != 'kalu'})	


# set comprehension
nums = [1,1,1,1,2,2,2,55,5]
set_1 = {x for x in nums}
print(set_1)

# generator comprehension

num = [1,2,3,4,5,6,7]

def gen(num):
	for n in num:
		yield n*n
my_gen = gen(num)

print(my_gen)

for i in my_gen:
	print(i)






