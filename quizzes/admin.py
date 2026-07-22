from django.contrib import admin
from .models import Quiz,QuizAttempt,QuizQuestion
# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizAttempt)
admin.site.register(QuizQuestion)