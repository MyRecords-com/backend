from django.shortcuts import render
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
  
class ReactView(APIView):
    
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

    serializer_class = RecordSerializer
    
    def get(self, request):
        detail = [ {"name": detail.name, "label": detail.label, "country": detail.country, "rec_format": detail.rec_format, "released": detail.released, "genre": detail.genre, "style": detail.style} 
        for detail in Record.objects.all()]
        return Response(detail)

class ProfileView(APIView):

    serializer_class = ProfileSerializer
    
    def get(self, request):

        # profile = Profile.objects.get(location="Hong Kong, CN")
        
        user = [ {"username": profile.user.username, "first_name": profile.user.first_name, "last_name": profile.user.last_name, "location": profile.location, "setup": profile.setup, "bio": profile.bio, "created_date": profile.created_date}
        for profile in Profile.objects.all()    
        ]
        # return Response(user)
        return Response(user)
        # profile = [ {"name": detail.name, "label": detail.label, "country": detail.country, "rec_format": detail.rec_format, "released": detail.released, "genre": detail.genre, "style": detail.style} 
        # for detail in Record.objects.all()]
        # return Response(profile)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)