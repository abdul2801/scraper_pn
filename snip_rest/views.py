from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnipperSerializer as SnippetSerializer
# Create your views here.
import requests
import json
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
from .myntra import Myntra

class List_View(APIView):
	@csrf_exempt
	def get(self,request,search):
		print(search)
		# serializer = SnippetSerializer(Snippet.objects.all(),many=True)
		headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
		
		M = Myntra()
		page = request.GET.get('p','1')
		print(page)
		M.params['rawQuery'] = search
		M.params['p'] = page

		res = M.get_item_list()
		

		return Response(res)

	def post(self,request,format=None):
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)

		
		
		if(serializer.is_valid()):
			serializer.save()

			return Response(serializer.data,status=status.HTTP_201_CREATED,)
		
		else:
			return Response("400 BAD REQUEST", status=status.HTTP_400_BAD_REQUEST)

