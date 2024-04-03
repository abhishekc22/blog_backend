from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Blog
        fields = '__all__'  

class Getblogserializer(serializers.ModelSerializer): 
     model = Blog
     fields = '__all__'  
     depth=2

class Commentserializer(serializers.ModelSerializer):
    model=Comment
    fields = '__all__'  
    depth=2


class Replieserializer(serializers.ModelSerializer):
    model=Replies
    fields='__all__'
    depth=2