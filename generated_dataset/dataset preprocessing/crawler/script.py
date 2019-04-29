import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
driver=webdriver.Chrome('/usr/bin/chromedriver')


r = requests.get("https://arxiv.org/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first")
soup = BeautifulSoup(r.content, "html.parser")
x = soup.find_all(class_="title is-5 mathjax")
for item in x:
	print item.get_text()
print("================================================================================")
