from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .supabase_client import supabase
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import logging
import uuid
from django.core.paginator import Paginator
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import serializers as drf_serializers
from .custom_auth import SupabaseAuthentication
from django.urls import reverse
logger = logging.getLogger(__name__)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email', 'password'],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        },
    ),
    responses={
        200: openapi.Response('Successful Login', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING, description='Access token'),
            }
        )),
        400: 'Bad Request'
    }
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({'error': 'You must provide both an email and a password'}, status=400)
    
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return Response({'token': response.session.access_token})
    except Exception as e:
        return Response({'error': str(e)}, status=400)

logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        # Get the token from the request
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        logger.info(f"Auth header: {auth_header}")
        
        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            logger.info(f"Token: {token}")
            
            # Sign out the user in Supabase
            response = supabase.auth.sign_out()
            logger.info(f"Supabase sign out response: {response}")
            
            return JsonResponse({'message': 'Logged out successfully'})
        else:
            return JsonResponse({'error': 'Invalid authorization header'}, status=400)
    except Exception as e:
        logger.error(f"Error in logout view: {str(e)}", exc_info=True)
        return JsonResponse({'error': str(e)}, status=400)