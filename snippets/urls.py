from django.urls import path
from snippets.views import all_snippets,cur_snippet

urlpatterns = [
	path('snippets',all_snippets),
	path('snippets/<int:id>',cur_snippet)
]