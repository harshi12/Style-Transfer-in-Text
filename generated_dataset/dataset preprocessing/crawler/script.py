import time
import requests 
from bs4 import BeautifulSoup
# from selenium import webdriver
# driver=webdriver.Chrome('/usr/bin/chromedriver')
# f = open("titles",'a')
i = 0
for i in range(0,200000,200):
	print(i)
	if i%2000 == 0:
		time.sleep(6)
	r = requests.get("https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-physics_archives=all&classification-statistics=y&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size="+str(200)+"&order=-announced_date_first&start="+str(i+200))
	time.sleep(2)
	soup = BeautifulSoup(r.content, "html.parser")
	x = soup.find_all(class_="title is-5 mathjax")
	for item in x:
		p = item.get_text().encode('utf-8')
		f.write(p)
		print p




#-=======================================================================
# link = driver.find_element_by_link_text('Next\n')
# link = soup.find_all(class_="pagination-next").click()
# link=driver.find_element_by_xpath([@class_="pagination-next"])

# link.click()

# for i in driver.find_element_by_partial_link_text(Next\n 	'):
    # i.click()
# driver.find_element_by_xpath("(//a[contains(text(),'Next')])[i]").click()
# import re
# link.click()

# soup.find_all(class_='pagination-next', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
# for l in link:
	# x = l.get('href')
	# print(type(x)) 
# link = driver.find_element_by_link_class_name('pagination-next')
# link = driver.find_element_by_css_selector('p.pagination-next')
# link = soup.find_all('a')
# print type(link)
# print soup.find( class='pagination-next')
# l = soup.find_all('a',attrs={'class':'pagination-next'})
# link = l.get_text('href')
# print "LINK FOR NEXT PAGE",link

# link.click()
# r = requests.get("https://arxiv.org/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first")
# soup = BeautifulSoup(r.content, "html.parser")
# x = soup.find_all(class_="title is-5 mathjax")

# for item in x:
# 	print item.get_text()

