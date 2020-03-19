# navigate through the file system
# rename file and whole lot of other thing
# with files


import os

#print(dir(os))

# print(os.getcwd())
# #os.makedirs('demo2/demo1')



# #os.rmdir('demo2')

# # lets rename a file
# #os.rename('sorting.py', 'sorting_new.py')
# print(os.listdir())

# from datetime import datetime
# mod_time = os.stat('sorting_new.py').st_mtime

# print(datetime.fromtimestamp(mod_time))

# generator os.walk()

# for dirpath, dirname, filename in os.walk(os.getcwd()):
# 	print(filename)
# 	print(dirpath)

# get env variable
print(os.environ.get('HOME'))	


file_path = os.path.join(os.environ.get('HOME'),'test.txt')

print(file_path)

with open(file_path, 'w') as f:
	f.write('hi how are you')

print(file_path)

print(os.path.split(file_path))
print(os.path.splitext(file_path))

print(dir(os.path))

