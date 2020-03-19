courses = ['History','english','hindi','art']

print(len(courses))

print(courses[0])

print(courses[-1])

# slicing

print(courses[::-1])

# add an item to the list
courses.append('maths')
print(courses)

# insert at a specific location
courses.insert(0, 'chemistrty')
print(courses)

# extend method - when we have to add mutiple value to the list
courses.extend(['physics','drawing'])
print(courses)

# remove values 
courses.remove('maths')
print(courses)

subject = courses.pop()
print(courses)

print(f'{subject}')
# stack can be created using append and pop method
# reverse the list
courses.reverse()
print(courses)

# sort the list
courses.sort()
print(courses)

nums = [5, 3, 2, 1, 7, 0]

nums.sort(reverse=True)
print(nums)

# without altering the original list we can use the sorted function

changedList = sorted(nums)
print(f'changed list wihich is sorted {changedList}')
print(nums)


# min of a list - min, max , sum
print(sum(nums))


# find the index of a certain value
print(courses.index('english'))

# check if value is not in list
print('english' in courses)
print('maths' in courses)

# loop over the list
for course in courses:
	print(course, end = ", ")

# access the index and value at the same time - use enumerate
for course in enumerate(courses, start=10):
	print(course)

# convert the list of courses in string
coursesString = ", ".join(courses)

print(coursesString)

print(type(coursesString))

# turn the string back into the list

courses_new = coursesString.split(",")
print(courses_new)

# tuples -----

# tuples are immutable

print(courses) 

courses1 = courses
print(courses1)

courses.append('biology')
print(courses)
print(courses1)

tuple_1 = ('A','B','C','D')

tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple is immutable
#tuple_1[0] = 'Z'

# set are unorderd and no duplicates allowed
# set does not care about ordered
set_1 = {'A','B','C','D','A','B'}
print(set_1)

print('C' in set_1)

set_2 = {'A','Z'}

print(set_1 - set_2)
print(set_1.difference(set_2))
print(set_1.union(set_2))
print(set_1.intersection(set_2))

# create empty list set and tuples
empty_set = set()
print(type(empty_set))
empty_list = []

empty_tuple = ()

# empty_set = {} will create an empty dictionary, NOT set


# dictionaries , key- value pairs
# key is unique identifier

dict_1 = dict()
print(type(dict_1))

dict_1 = {'name':'deepak','age':34, 'courses':['math', 'computer']}
print(dict_1)

print(dict_1['courses'])
print(dict_1['age'])
print(dict_1.get('phone','not here'))
print(dict_1.get('name'))

# add a key value pair
dict_1['phone'] = 12345
print(dict_1)

print(dict_1.get('phone'))


print(dict_1)

print(dict_1.update({'name':'kanishk', 'age':5}))

print(dict_1)

# delete a specific key
del dict_1['phone']


print(dict_1)
age = dict_1.pop('age')
print(f'age is {age}')


print(len(dict_1))

for key, value in dict_1.items():
	print(key, value)




