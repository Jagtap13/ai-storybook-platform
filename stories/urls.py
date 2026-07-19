from django.urls import path
from .views import StoryDetailView,StoryGenerateView,StoryListView

urlpatterns = [
    path('generate/',StoryGenerateView.as_view(),name="story-generate"),
    path(' ',StoryListView.as_view(),name="story-list"),
    path('<int:pk>/',StoryDetailView.as_view(),name="story-detail"),
]
