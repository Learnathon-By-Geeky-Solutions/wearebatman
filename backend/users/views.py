from rest_framework import viewsets
from .models import ParentUser, ChildUser
from .serializers import ParentUserSerializer, ChildUserSerializer

class ParentUserViewSet(viewsets.ModelViewSet):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserSerializer
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class ChildUserViewSet(viewsets.ModelViewSet):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserSerializer
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)