from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from stories.models import Story
from .models import Quiz,QuizAttempt,QuizQuestion
from .serializers import QuizAttemptSerializer,QuizSerializer

# Create your views here.
class QuizGenerateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, story_id):
        story = Story.objects.get(id=story_id,student=request.user.studentprofile)
        # TEMPORARY placeholder — will be replaced with real Gemini call later
        quiz = Quiz.objects.create(story=story)

        QuizQuestion.objects.create(
            quiz=quiz,
            question_type='mcq',
            question_text='What was the main setting of the story?',
            options=['A forest','A city','The ocean','Outer space'],
            correct_answer = 'A forest' ,
        )

        QuizQuestion.objects.create(
            quiz=quiz,
            question_type='true_false',
            question_text='The hero went on a journey.',
            options=['Ture','False'],
            correct_answer='True'
        )

        QuizQuestion.objects.create(
            quiz=quiz,
            question_type='vocabulary',
            question_text='what does "advanture" mean?',
            options=['A boring day', 'An exciting journey', 'A type of food', 'A color'],
            correct_answer='An exciting journey',
        )
        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class QuizDetailView(generics.RetrieveAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    queryset = Quiz.objects.all()
    
class QuizSubmitView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        answers = request.data.get('answers',{})

        questions = quiz.questions.all()
        total = questions.count()
        correct_count = 0

        result = []
        for question in questions:
            submitted = answers.get(str(question.id),'')
            is_correct = submitted == question.correct_answer
            if is_correct:
                correct_count += 1

            result.append({
                'question_id':question.id,
                'question_text': question.question_text,
                'submitted_answer': submitted,
                'correct_answer': question.correct_answer,
                'is_correct': is_correct,
            })
        score = round((correct_count / total) * 100 ) if total > 0 else 0

        attempt = QuizAttempt.objects.create(
            quiz=quiz,
            student=request.user.studentprofile,
            score=score,
        )
        return Response({
            'attempt_id':attempt.id,
            'score':score,
            'correct_count':correct_count,
            'total_question':total,
            'result':result,
        }, status=status.HTTP_200_OK)
            