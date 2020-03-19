
import requests
from bs4 import BeautifulSoup
import csv

# # get the file
# with open('sample.html') as html_file:

# 	soup = BeautifulSoup(html_file, 'lxml')

# 	#print(soup.prettify())


# 	all_div = soup.findAll('div', class_='article')
# 	for article in all_div:
# 		headline = article.h2.text
# 		print(headline)
		

# 		summary = article.p.text
# 		print(summary)
# 		print()
# 	



source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

csv_file = open('coreywebsite_scraped.csv','w')
csvwriter = csv.writer(csv_file)

csvwriter.writerow(['headline','description','youtube links'])

for article in soup.find_all('article'):
#print(article.prettify())

	headline = article.a.text
	print(headline)

	description = article.find('div', class_='entry-content')
	description = description.p.text
	print(description)

	
	

	try:
		video_link = article.find('iframe', class_='youtube-player')
		video_link = video_link['src']

		video_id = video_link.split('?')[0]
		video_id = video_id.split('/')[-1]
		yt_link = f'https://youtube.com/watch?v={video_id}'
	except Exception as e:
		yt_link = None

	print(yt_link)


	print()
	csvwriter.writerow([headline, description, yt_link])

csv_file.close()




