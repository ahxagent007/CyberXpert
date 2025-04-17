from django.shortcuts import render
from .models import Questions, Level



def Quiz(request, level_no):
    question_list = Questions.objects.filter(level_number=level_no)
    level = Level.objects.get(number = level_no)
    data = {
        'question_list': question_list,
        'level': level.name,
        'level_description': level.description,
        'level_no': level_no
    }
    return render(request=request, template_name='lesson/quiz.html', context=data)
