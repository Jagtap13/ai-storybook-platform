from django.db import models
from stories.models import Story
from users.models import StudentProfile

# Create your models here.
class Quiz(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE,related_name="quiz")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz for {self.story.title}"
    
class QuizQuestion(models.Model):
    QUESTION_TYPE = (
        ('mcq','Multiple Choice'),
        ('true_false','True/False'),
        ('vocabulary','vocabulary'),
    )

    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="questions")
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE)
    question_text = models.TextField()
    options = models.JSONField(default=list, blank=True)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text[:50]
    
class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="attempts")
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE,related_name="quiz_attemptes")
    score = models.PositiveIntegerField()
    time_taken_sec = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.quiz} - {self.score}"
