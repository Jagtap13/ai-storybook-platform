from django.db import models
from users.models import StudentProfile


# Create your models here.
class Story(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="stories")
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=50)
    difficulty = models.CharField( max_length=20)
    moral_theme = models.CharField( max_length=100,blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class StoryPage(models.Model):
    story = models.ForeignKey(Story,on_delete=models.CASCADE,related_name="pages")
    page_number = models.PositiveBigIntegerField()
    text = models.TextField()

    class Meta:
        ordering = ['page_number']

    def __str__(self):
        return f"{self.story.title} - Page {self.page_number}"
    