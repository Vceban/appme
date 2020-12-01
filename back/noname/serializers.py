from rest_framework import serializers
from noname.models import Info

class InfoSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Info
		fields	= '__all__'