import requests
from requests import get
from bs4 import BeautifulSoup as beauty

#To get currencies values and stuff
def getvalues(content):
	currencies = ''
	currencies += "\nMonitor-dolar-venezuela: " + "\n\n"
	for tag in content:
		ptag = tag.find_all('p')
		for p in range(len(ptag)-2):
			currencies += " " * 4 + (ptag[p].text) + '\n'
	return currencies

links = ["https://monitordolarvenezuela.com/"]
page = get(links[0])
if page.status_code == 200:
	cont = beauty(page.content, 'html.parser').find_all(class_ = 'box-calcmd text-center')
	curr_values = getvalues(cont)
else:
	curr_values = "Por el momento no pude localizar los datos, disculpa."
