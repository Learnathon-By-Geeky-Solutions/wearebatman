from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentUserViewSet, ChildUserViewSet

router = DefaultRouter()
router.register(r'parents', ParentUserViewSet, basename='parentuser')
router.register(r'children', ChildUserViewSet, basename='childuser')

urlpatterns = [
    path('', include(router.urls)),
]