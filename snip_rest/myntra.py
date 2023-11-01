import requests
import json
from bs4 import BeautifulSoup
import urllib.parse

class Myntra:
	def __init__(self):
		self.headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
		self.url = "https://www.myntra.com"

		self.params = {'rawQuery' : "" , 'p' : "1"}
		self.session = requests.Session()

	def url_gen(self):
		search = self.params['rawQuery'].replace(" ", "_")
		url = f'{self.url}/{search}/?'

		for p,v in self.params.items():
			url = f'{url}{p}={urllib.parse.quote(v)}&'

		return url

	def get(self):
		res = self.session.get(self.url_gen(), headers=self.headers, verify=False)
		
		soup = BeautifulSoup(res.text,"lxml")
		
		script = None
		for s in soup.find_all("script"):
		    if 'itemListElement' in s.text:
		        script = s.get_text(strip=True)
		       
		        break

		return json.loads(script[script.index('{'):])

	def get_item(self,url):
		res = self.session.get(url, headers=self.headers, verify=False)

		soup = BeautifulSoup(res.text,"lxml")

		script = None
		for s in soup.find_all("script"):
			if 'pdpData' in s.text:
				script = s.get_text(strip=True)
				break

		return (json.loads(script[script.index('{'):]))

	def get_item_list(self):
		res = self.get()['itemListElement']

		response = {}
		for i in range(len(res)):
			response[i] = res[i]
			url = res[i]['url']
				# response.append(self.get_item(url))
			

			item = self.get_item(url)['pdpData']
			media = item['media']
			mrp = item['price']['discounted']

			response[i]['media'] = media
			response[i]['mrp'] = mrp
			
		return json.dumps(response)
		

		












