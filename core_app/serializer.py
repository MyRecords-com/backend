from rest_framework import serializers
from . models import *
  
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['name', 'label', 'country', 'rec_format', 'released', 'genre', 'style']
