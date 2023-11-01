from django.db import models

# Create your models here.
class Snippet(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.TextField(max_length=40)
	def __str__(self):
		return self.title