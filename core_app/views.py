from urllib import request
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status, viewsets, generics
from core_app.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
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
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from .serializer import ProfileSerializer
from rest_framework.authtoken.models import Token
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
        '/token/',
        '/register/',
        '/token/refresh/',
        '/prediction/',
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

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getProfiles(request):
    datas = Profile.objects.get(user=request.user)

    if request.method == 'GET':
        data = f"Congratulation {datas.user.email}, your API just responded to GET request"
        return Response({'response': data})
   
    # user = request.user
    # profiles = user.profile_set.all()
    # serializer = ProfileSerializer(profiles, many=True)
    # return Response(serializer.data)

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
    permission_classes = [IsAuthenticated]
    serializer_class = RecordSerializer
    
    def get(self, request):
        detail = [ {"name": detail.name, "label": detail.label, "country": detail.country, "rec_format": detail.rec_format, "released": detail.released, "genre": detail.genre, "style": detail.style} 
        for detail in Record.objects.all()]
        return Response(detail)

    def post(self, request):
        if request.method == 'POST':
          data = request.data
          collection = data['collection']
          name = data['name']
          label = data['label']
          country = data['country']
          recformat = 'Vinyl 12'
          released = data['released']
          genre = data['genre']
          style = data['style']
          
          addedRecord = Record.objects.create(name=name, label=label, country=country, rec_format=recformat, released=released, genre=genre, style=style)
          addedCollection = Collection.objects.filter(name=collection)
        #   addedCollection.objects.create(name=)
          return Response('Record Added to Your Collection!') 
    
    
    # def get(self, request):
    #     return Response(print(request.auth))

        # datas = Collection.objects.get(user=request.user)

        # if request.method == 'GET':
        #     data = f"Congratulation {datas.user.username}, your API just responded to GET request"
        #     return Response({'response': data})

        # collectionData = [{ 'name': data.name, 'description': data.description, 'records': data.records }]
        # return Response(collectionData)


# @api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
class ProfileView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        datas = Profile.objects.get(user=request.user)
        if request.method == 'GET':
            # data = f"Congratulation {datas.user.first_name}, your API just responded to GET request"
            # return Response({'response': data})


            profileData = {'user': datas.user.username, 'created_date': datas.created_date, 'location': datas.location, 'usr_type': datas.usr_type, 'setup': datas.setup, 'bio': datas.bio}
            return Response(profileData)


class CollectionView(APIView):
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request):
        
        
        if request.method == 'GET':
            collection = Collection.objects.filter(user__user=self.request.user)
            # collections = { 'name': collection.name, 'description': collection.description }
            serializer = CollectionSerializer(collection, many=True)
            # recordss = Collection.objects.get(user__user=self.request.user)
            # allRecords = recordss.records
            # serializer = RecordSerializer(allRecords, many=True)
            return Response(serializer.data)

        
        
        
        # access_token_obj = AccessToken(request.auth)
    # permission_classes = [AllowAny]
    # # serializer_class = ProfileSerializer
    # # serializer_class = MyTokenObtainPairSerializer
    # def post(self, request):
    #     data = JSON.parse(request.data)
        
    #     print(data)
    #     return Response(data)
    # def get(self, request):
    #     access_token_str = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzQzNTIxNiwiaWF0IjoxNjU5MTE1MjE2LCJqdGkiOiJmNzI5YWRhNDRlYWY0MjFiYWMxNWY4NzU3Yzg2MDczYSIsInVzZXJfaWQiOjd9.Sfj1tMqs2kjYTBAhyzi0_PKA9FvrszrG0eZCMcI3Xys'
    #     access_token = AccessToken(access_token_str)
    #     user = User.objects.get(access_token['user_id'])
    #     print(user)
    # def post(self, request, format=None):
    #     token_user_email = request.user
    #     print(token_user_email)
    #     return Response(token_user_email)
    
    # access_token_str = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU5MTE1NTE2LCJpYXQiOjE2NTkxMTUyMTYsImp0aSI6ImQ5ZmE2Zjk0Y2RiMDQxNmRhN2NmOTY3MWNhNjVmOWQ2IiwidXNlcl9pZCI6NywidXNlcm5hbWUiOiJtaWxlc3Rlc3Q4OCIsImVtYWlsIjoiIn0.Jd5y_d1uELq3HmZf735oUcSbaAYESYsK761RiR0jCaE'
    # def get_user_from_access_token_in_django_rest_framework_simplejwt(access_token_str):
    #     access_token_obj = AccessToken(access_token_str)
    #     user_id=access_token_obj['user_id']
    #     user=User.objects.get(id=user_id)
    #     print('user_id: ', user_id )
    #     print('user: ', user)
    #     print('user.id: ', user.id )
    #     content =  {'user_id': user_id, 'user':user, 'user.id':user.id}
    #     return Response(content)










    # def get(self, request):

        # profile = Profile.objects.get(location="Hong Kong, CN")
        # user = [ {"username": profile.user.username, "first_name": profile.user.first_name, "last_name": profile.user.last_name, "location": profile.location, "setup": profile.setup, "bio": profile.bio, "created_date": profile.created_date}
        # for profile in Profile.objects.all()    
        # ]
        # print(token['username'])
        # specificUser = User.objects.get(username==request.user.username)
        # print(specificUser)
        # returnedData = [ { "description": specificUser.description } ]
        # userCollection = [{ "description": specificUser.description, "records": specificUser.records } for collections in Collection.objects.all()]
        # return Response()
        # return Response()
        # profile = [ {"name": detail.name, "label": detail.label, "country": detail.country, "rec_format": detail.rec_format, "released": detail.released, "genre": detail.genre, "style": detail.style} 
        # for detail in Record.objects.all()]
        # return Response(profile)
