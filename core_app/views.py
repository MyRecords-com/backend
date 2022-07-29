from urllib import request
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status, viewsets, generics
from core_app.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


# Create your views here.
  
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/prediction/',
        # '/core/todo/'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def EndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)



class ReactView(APIView):
    permission_classes = [AllowAny]    
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = [ {"name": detail.name,"detail": detail.detail} 
        for detail in React.objects.all()]
        return Response(detail)
  
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)

class RecordView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RecordSerializer
    
    def get(self, request):
        detail = [ {"name": detail.name, "label": detail.label, "country": detail.country, "rec_format": detail.rec_format, "released": detail.released, "genre": detail.genre, "style": detail.style} 
        for detail in Record.objects.all()]
        return Response(detail)

class ProfileView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer
    
    def get(self, request):

        # profile = Profile.objects.get(location="Hong Kong, CN")
        

        user = [ {"username": profile.user.username, "first_name": profile.user.first_name, "last_name": profile.user.last_name, "location": profile.location, "setup": profile.setup, "bio": profile.bio, "created_date": profile.created_date}
        for profile in Profile.objects.all()    
        ]

        specificUser = Collection.objects.get(user=request.username)
        userCollection = [{"clt_name": specificUser.name "description": specificUser.description "records": specificUser.records } for collection in Collection.objects.all()]
        # return Response(user)
        return Response(user, userCollection)
        # profile = [ {"name": detail.name, "label": detail.label, "country": detail.country, "rec_format": detail.rec_format, "released": detail.released, "genre": detail.genre, "style": detail.style} 
        # for detail in Record.objects.all()]
        # return Response(profile)
