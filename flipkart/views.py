from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# Create your views here.
import requests
import json
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
from .flip import Flipkart_C

class List_View(APIView):
	@csrf_exempt
	def get(self,request,search):
		
		M = Flipkart_C()
		page = request.GET.get('p','1')
		print(page)
		M.params['q'] = search
		M.params['page'] = page

		res = M.get()
		

		return Response(res)
