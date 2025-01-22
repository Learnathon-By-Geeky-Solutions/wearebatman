from rest_framework import viewsets
from .models import ParentUser, ChildUser
from .serializers import ParentUserSerializer, ChildUserSerializer

class ParentUserViewSet(viewsets.ModelViewSet):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserSerializer

class ChildUserViewSet(viewsets.ModelViewSet):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserSerializer