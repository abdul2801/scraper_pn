from .views import List_View 
from django.urls import path


urlpatterns = [
	path("<search>/",List_View.as_view())
]