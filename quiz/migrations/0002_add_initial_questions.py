# quiz/migrations/0002_add_initial_questions.py

from django.db import migrations

def create_initial_questions(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')
    initial_questions = [
        {
            'question_text': 'What is the capital of France?',
            'option_a': 'Berlin',
            'option_b': 'Madrid',
            'option_c': 'Paris',
            'option_d': 'Rome',
            'correct_option': 'C',
        },
        {
            'question_text': 'Which planet is known as the Red Planet?',
            'option_a': 'Earth',
            'option_b': 'Mars',
            'option_c': 'Jupiter',
            'option_d': 'Saturn',
            'correct_option': 'B',
        },
        {
            'question_text': 'What is the largest ocean on Earth?',
            'option_a': 'Atlantic Ocean',
            'option_b': 'Indian Ocean',
            'option_c': 'Arctic Ocean',
            'option_d': 'Pacific Ocean',
            'correct_option': 'D',
        },
    ]

    for q in initial_questions:
        Question.objects.create(
            question_text=q['question_text'],
            option_a=q['option_a'],
            option_b=q['option_b'],
            option_c=q['option_c'],
            option_d=q['option_d'],
            correct_option=q['correct_option'],
        )

class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),  # Ensure this matches your last migration
    ]

    operations = [
        migrations.RunPython(create_initial_questions),
    ]
