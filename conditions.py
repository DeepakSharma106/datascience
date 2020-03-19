lang = 'Java'


if lang == 'python':
	print('lang is python')

elif  lang == 'Java':
	print('lang is java')

else:
	print('no match')


logged_in = False
user = 'Admin'

if user == 'Admin' and logged_in:
	print('admin is logged in')

else:
	print('someone else is logged in')


if not logged_in:
	print('please log in')
else:
	print('you are already logged in ')


a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(a == b)

print(a is b)

c = [5,6]
d = [5,6]

c = d

print(c == d)
print(c is d)

# is operator simple check if two variable have same memory location
# == operator check the equivalenc of content, if content is equal or not

# not null check is 
if not None:
	print('i am not null')

condition = None
if not condition:
	print('evaluated to true')
else:
	print('evaluated to false')


# chekcing for empty list or set or dict
list1 = []

if list1:
	print('not empty')
else:
	print('empty')