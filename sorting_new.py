tup = (7,11,5,4,3,2,1)

print(tup)

sorted_tup = sorted(tup)

print('sorted\t',sorted_tup)

dic = {'name':'deepak','age':34,'profession':'coder'}

print(dic)

sorted_dic = sorted(dic)

print('sorted\t', sorted_dic)

li = [1,6,-1, 3, 2, -2]

sorted_li = sorted(li, key=abs)

print(sorted_li)

class Employee:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return f'{self.name} & {self.age} & {self.salary}'

from operator import attrgetter

e1 = Employee('deepak', 34, 4500)
e2 = Employee('shagun', 24, 3500)
e3 = Employee('lavanya', 14, 6500)
e4 = Employee('kanishk', 4, 5500)

empList = [e1, e2, e3, e4]
print(empList)

def e_sort(emp):
	return emp.name

sorted_empList = sorted(empList, key=attrgetter('age'))
print(sorted_empList)

pi = 3.147821

print(f'{pi:.3f}')


