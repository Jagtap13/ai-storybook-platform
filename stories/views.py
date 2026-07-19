from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Story , StoryPage
from .serializers import StorySerializer

# Create your views here.

class StoryGenerateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        topic = request.data.get('topic','adventure')
        difficulty = request.data.get('difficulty','easy')

        student_profile = request.user.studentprofile

        # Temporary placeholder - will be replaced after gemini real call after 
        story = Story.objects.create(
            student=student_profile,
            title=f"{topic.title()} Advanture",
            topic=topic,
            difficulty=difficulty,
            moral_theme="Sharing is Caring."
        )

        StoryPage.objects.create(story=story,page_number=1,text= "once upon a time in a farway land...")
        StoryPage.objects.create(story=story,page_number=2,text= "A young hero set out an a journey...")
        StoryPage.objects.create(story=story,page_number=3,text= "They all lived happly even after...")

        serializer = StorySerializer(story)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
class StoryListView(generics.ListAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Story.objects.filter(student=self.request.user.studentprofile)
    
class StoryDetailView(generics.RetrieveAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Story.objects.all()

