from rest_framework import serializers
from .models import Snippet

class SnipperSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = '__all__'
