from .models import Info
from rest_framework import viewsets,permissions
from .serializers import InfoSerializer

class InfoViewSet(viewsets.ModelViewSet):

	queryset = Info.objects.all()
	permissions_classes = [ 
		permissions.AllowAny
	]
	serializer_class = InfoSerializer