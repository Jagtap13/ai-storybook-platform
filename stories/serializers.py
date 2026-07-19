
from rest_framework import serializers
from .models import Story , StoryPage

class StoryPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryPage
        fields = ['page_number','text']

class StorySerializer(serializers.ModelSerializer):
    pages = StoryPageSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ['id','title','topic','difficulty','moral_theme','created_at','pages']