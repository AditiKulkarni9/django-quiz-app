from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/', views.get_question, name='get_question'),
    path('submit/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('stats/', views.stats, name='stats'),
    path('quiz-admin/questions/add/', views.add_question, name='add_question'),
    path('quiz-admin/questions/', views.view_questions, name='view_questions'),
]
