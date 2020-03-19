# file objects
import os
with open('test.txt','r') as rf:
	with open('test_copy.txt','w') as wf:
		for line in rf:
			wf.write(line)

	

#print(f.closed)
print(os.getcwd())

for f in os.listdir():
	#print(f)
	filename, fileext = os.path.splitext(f)
	#print(filename, fileext)
	l_filename = filename.lower()

	#print(type(filename))
	#print(dir(str))
	new_name = f'{l_filename}{fileext}'
	os.rename(f, new_name)