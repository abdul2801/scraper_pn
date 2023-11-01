from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnipperSerializer as SnippetSerializer
import requests
import json
from bs4 import BeautifulSoup
@csrf_exempt
def all_snippets(request):

	if request.method == "GET":

		headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
		
		s = requests.Session()
		res = s.get("https://www.myntra.com/sports-shoes/puma/puma-men-blue-hybrid-fuego-running-shoes/11203218/buy", headers=headers, verify=False)
		
		soup = BeautifulSoup(res.text,"lxml")
		
		script = None
		for s in soup.find_all("script"):
		    if 'pdpData' in s.text:
		        script = s.get_text(strip=True)
		        break

		res = json.loads(script[script.index('{'):])

		# serializer = SnippetSerializer(Snippet.objects.all(),many=True)
		# print(doujin)
		print(res['0'])
		return JsonResponse(res,safe=False)
		

	elif request.method == 'POST':
		
		data = JSONParser().parse(request)
		print(data)
		serializer =  SnippetSerializer(data=data)
		if(serializer.is_valid()):
			serializer.save()
			return JsonResponse(serializer.data)
		else:
			return HttpResponse(status=400)

@csrf_exempt
def cur_snippet(request,id):
	try:
		snippet = Snippet.objects.get(id=id)
	except:
		return HttpResponse("404 NOT FOUND",status=404)

	if(request.method == "GET"):
		data = SnippetSerializer(snippet).data
		return JsonResponse(data)

	elif(request.method == "DELETE"):
		data = SnippetSerializer(snippet).data
		snippet.delete()
		return JsonResponse(data)