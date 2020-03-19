
print('using function module')
def find_index(to_search, target):
	for i, value in enumerate(to_search):
		if value == target:
			return i
	return -1

test = 'iam using string'


