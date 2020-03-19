
class MyRange:

	def __init__(self, start, end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration

		current = self.value
		self.value += 1
		return current

def my_range(start, end):
	current = start
	while(current < end):
		yield current
		current += 1


nums = my_range(1, 5)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
#print(next(nums))
#print(next(nums))

# for n in nums:
# 	print(n)


import itertools

counter = itertools.count()

data = [10, 20, 30]

result = list(zip(counter, data))

test = list(enumerate(data))
print(test)

print(result)
# print(next(counter))
# print(next(counter))
# print(next(counter))