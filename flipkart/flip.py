from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
import urllib.parse
import json


class Flipkart_C:
	def __init__(self):
		self.headers = {
    	'Cookie': 'T=TI169495825217200191078969303037775990847788829254234223621971195089; SN=VI24B0B7EEDBA04DBC8D65E37FF0F8D9B4.TOK63862A62728045EA96E68CD6B340E3C9.1698249139.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE2OTk5NzcxMzksImlhdCI6MTY5ODI0OTEzOSwiaXNzIjoia2V2bGFyIiwianRpIjoiODk4ZjFlMGUtNWY5OS00ZGQyLTliZTUtMGU3NmM4YTI4NDdiIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjk0OTU4MjUyMTcyMDAxOTEwNzg5NjkzMDMwMzc3NzU5OTA4NDc3ODg4MjkyNTQyMzQyMjM2MjE5NzExOTUwODkiLCJrZXZJZCI6IlZJMjRCMEI3RUVEQkEwNERCQzhENjVFMzdGRjBGOEQ5QjQiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.jLs1nogrY5dcURE_xe1JxmTlFRXrByf4zOkoN6hKFrQ; K-ACTION=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19656%7CMCMID%7C45005039654451277202692784773422575877%7CMCAID%7CNONE%7CMCOPTOUT-1698256334s%7CNONE; S=d1t11H1c/VG47Az9mfT8/Pz9jXE5uPO3cpguBsaFTk72aiYAlpSSMnH5VUlhe9tnESMn/VB3Gsp5o+BZ95X9kyLGnxw==; vh=672; vw=1280; dpr=1.25; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; qH=c06ea84a1e3dc3c6; gpv_pn=Search%20%3AComputers%7CLaptops; gpv_pn_t=Search%20Page; s_cc=true',
    	'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
    	'Connection' : "keep-alive",
    	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
		}
		self.url = "https://www.flipkart.com/search"
		self.params = {"q" : "" , "page" : "1"}
		self.session = requests.Session()



	def url_gen(self):
		self.params['q'] = self.params['q'].replace("_", " ")

		url = self.url + "?"

		for p,v in self.params.items():
			url = f'{url}{p}={urllib.parse.quote(v)}&'

		return url


	def different_parse(self,page_soup):
		res=[]
		container = page_soup.findAll("div",{"class":"_1xHGtK _373qXS"})
		if(not container): return self.differents_parse(page_soup)
		for cont in container:
			curres={}
			imgurl = cont.find(class_="_2r_T1I")['src']
			title = cont.find(class_="IRpwTa")['title']
			price = cont.find(class_="_30jeq3").text[1:]
			url = "https://www.flipkart.com"+cont.find(class_="_3bPFwb")['href']
			curres["name"] = title
			curres["price"] = price
			curres["rating"] = "4"
			curres["url"] = url
			curres["image"] = imgurl
			res.append(curres)

		return json.dumps({"products" : res})




	def differents_parse(self,page_soup):
		res=[]
		container = page_soup.findAll("div",{"class":"_4ddWXP"})

		for cont in container:
			curres={}
			imgurl = cont.find(class_="_396cs4")['src']
			# rating = cont.find(class_="_3LWZlK").text
			title = cont.find(class_="s1Q9rs")['title']
			price = cont.find(class_="_30jeq3").text[1:]
			url = "https://www.flipkart.com"+cont.find(class_="s1Q9rs")['href']
			curres["name"] = title
			curres["price"] = price
			curres["rating"] = "4"
			curres["url"] = url
			curres["image"] = imgurl
			res.append(curres)

		return json.dumps({"products" : res})

		
		

	def get(self):
		res = self.session.get(self.url_gen(), headers=self.headers, verify=False)
		page_soup = soup(res.content,"html.parser")
		# print(page_soup)
		container = page_soup.findAll("a",{"class":"_1fQZEK"})
		if(not container):
			return self.different_parse(page_soup)
		res=[]
		for cont in container:
		    curres = {}
		
		    innercontainer = cont.find("div",{"class":"_3pLy-c row"})
		    img = cont.find("div",{"class":"CXW8mj"})
		    # print(len(urls),len(containers),len(imgs))
		    url =  "https://www.flipkart.com"+cont['href']
		
		    title = innercontainer.find(class_="_4rR01T").text

		    
		    price = innercontainer.find(class_="_30jeq3 _1_WHN1").text[1:]
		    print(price)
		    imgurl = img.find("img")['src']

		    rating = innercontainer.find(class_="_3LWZlK")
		    if(not rating):
		    	rating = "No Rating"
		    else:
		    	rating = rating.text
		    
		
		    # print(price)
		    curres["name"] = title
		    curres["price"] = price
		    curres["rating"] = rating
		    curres["url"] = url
		    curres["image"] = imgurl
		    # title = 
		    res.append(curres)

		return json.dumps({"products" : res})
		
		
		
		



