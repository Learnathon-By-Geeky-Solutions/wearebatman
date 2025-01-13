from rest_framework import authentication
from rest_framework import exceptions
from .supabase_client import supabase
# import requests
from rest_framework import authentication, exceptions
from django.conf import settings
from django.db import transaction

class SupabaseUser:
    def __init__(self, supabase_user):
        self.id = supabase_user.id
        self.email = supabase_user.email
        self.is_authenticated = True
        self.is_active = True  # You might want to determine this based on Supabase user status

    @property
    def is_anonymous(self):
        return False

class SupabaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header:
            return None
        
        print("In supabase auth")

        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        else:
            token = auth_header  # Assume the entire header is the token

        try:
            user = supabase.auth.get_user(token)
            return (SupabaseUser(user.user), None)
        except Exception as e:
            raise exceptions.AuthenticationFailed('Invalid token')

    def authenticate_header(self, request):
        return 'Bearer'