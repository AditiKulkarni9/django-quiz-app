import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from django.contrib import messages
from .forms import QuestionForm

def start_quiz(request):
    request.session['answered_questions'] = []
    request.session['correct_count'] = 0
    request.session['incorrect_count'] = 0
    return render(request, 'index.html')

def get_question(request):
    all_questions = Question.objects.all()
    answered_ids = request.session.get('answered_questions', [])
    unanswered_questions = all_questions.exclude(id__in=answered_ids)

    if not unanswered_questions.exists():
        return redirect('stats')

    question = random.choice(list(unanswered_questions))
    return render(request, 'question.html', {'question': question})

def submit_answer(request, question_id):
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            return HttpResponse("Question does not exist.")

        answered_questions = request.session.get('answered_questions', [])
        if question_id not in answered_questions:
            answered_questions.append(question_id)
        request.session['answered_questions'] = answered_questions

        if user_answer == question.correct_option:
            request.session['correct_count'] = request.session.get('correct_count', 0) + 1
            is_correct = True
        else:
            request.session['incorrect_count'] = request.session.get('incorrect_count', 0) + 1
            is_correct = False

        return render(request, 'result.html', {
            'question': question,
            'user_answer': user_answer,
            'is_correct': is_correct
        })

def stats(request):
    correct = request.session.get('correct_count', 0)
    incorrect = request.session.get('incorrect_count', 0)
    answered = request.session.get('answered_questions', [])
    answered_questions = Question.objects.filter(pk__in=answered)
    return render(request, 'stats.html', {
        'correct_count': correct,
        'incorrect_count': incorrect,
        'total_answered': len(answered),
        'answered_questions': answered_questions
    })

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question added successfully!')
            return redirect('add_question')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})

def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})