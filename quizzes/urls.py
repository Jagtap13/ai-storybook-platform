from django.urls import path
from .views import QuizGenerateView, QuizDetailView, QuizSubmitView

urlpatterns = [
    path('generate/<int:story_id>/',QuizGenerateView.as_view(),name='quiz-generate'),
    path('<int:pk>/',QuizDetailView.as_view(),name='quiz-detail'),
    path('<int:quiz_id>/submit/',QuizSubmitView.as_view(),name='quiz-submit'),
]
