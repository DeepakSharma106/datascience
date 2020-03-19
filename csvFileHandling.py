import csv

# with open('names.csv','r') as fr:
# 	# content = fr.read()
# 	# print(content)
# 	# get csv reader
# 	csv_reader = csv.reader(fr)

# 	#print(csv_reader)
# 	#next(csv_reader)
# 	with open('newNames.csv','w') as newfile:
# 		csvwriter = csv.writer(newfile, delimiter='\t')




# 		for line in csv_reader:
# 			csvwriter.writerow(line)


with open('names.csv','r') as file:
	csvreader = csv.DictReader(file)

	with open('latest_names.csv','w') as new_file:
		fields = ['first_name', 'last_name']
		csvwriter = csv.DictWriter(new_file, fieldnames = fields)
		csvwriter.writeheader()

		for line in csvreader:
			del line['email']
			csvwriter.writerow(line)
