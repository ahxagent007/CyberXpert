from django.shortcuts import render, redirect
from .models import Questions, Level, AssignLevels, QuizPaper
from UserManager.decorators import login_access_only, admin_access_only
from UserManager.models import UserAccount
import os
from django.conf import settings
import requests
from .forms import AssignLevelsForm


@login_access_only()
def Quiz(request, level_no):
    question_list = Questions.objects.filter(level_number=level_no)
    level = Level.objects.get(number=level_no)

    if request.method == 'GET':

        captcha_sitekey = settings.RECAPTCHA_PUBLIC_KEY
        data = {
            'question_list': question_list,
            'level': level.name,
            'level_description': level.description,
            'level_no': level_no,
            'captcha_sitekey': captcha_sitekey
        }
        return render(request=request, template_name='lesson/quiz.html', context=data)
    elif request.method == 'POST':

        token = request.POST.get('g-recaptcha-response')

        # Verify with Google
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': token
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        print(result)

        total_answered = 0
        total_correct = 0
        total_question = len(question_list)

        # Check reCAPTCHA score
        if result.get('success') and result.get('score', 0) >= 0.5:
            data = request.POST

            for q in question_list:
                try:
                    user_answer = data['radio-' + str(q.id)]
                except:
                    user_answer = ''

                total_answered += 1

                if user_answer == q.answer:
                    total_correct += 1

                q.user_answer = user_answer


            user = UserAccount.objects.get(id=request.user.id)
            answer_no = len(QuizPaper.objects.filter(level=level, user=user)) + 1

            QuizPaper.objects.create(level=level, user_score=total_correct, total_questions=total_question,
                                     total_answered=total_answered, user=user,
                                     answer_no=answer_no)

            #return redirect('Dashboard:Message')
            data = {
                'question_list': question_list,
                'level': level.name,
                'level_description': level.description,
                'level_no': level_no
            }
            return render(request=request, template_name='lesson/quiz_result.html', context=data)

        else:
            data = {
                'question_list': question_list,
                'level': level.name,
                'level_description': level.description,
                'level_no': level_no,
                'error': 'reCAPTCHA verification failed. Please try again.',
                'captcha_sitekey': settings.RECAPTCHA_PUBLIC_KEY
            }
            # Possible bot or verification failed
            return render(request, template_name = 'lesson/quiz.html', context = data)

@login_access_only()
def QuizResult(request):
    level_no = 1
    question_list = Questions.objects.filter(level_number=level_no)
    level = Level.objects.get(number=level_no)

    data = {
        'question_list': question_list,
        'level': level.name,
        'level_description': level.description,
        'level_no': level_no
    }
    return render(request=request, template_name='lesson/quiz_result.html', context=data)



@login_access_only()
def LessonList(request):

    user = UserAccount.objects.get(id=request.user.id)

    assign_levels = AssignLevels.objects.filter(user=user)

    levels = {}

    for al in assign_levels:
        levels['id'+str(al.Level.id)] = al.Level

    data = {
        'levels': levels
    }
    return render(request=request, template_name='lesson/lesson_list.html', context=data)

@admin_access_only()
def AssignLevelsView(request):
    if request.method == 'POST':
        form = AssignLevelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lesson:AssignLevelsList')  # Redirect to a view that shows all books
    else:
        form = AssignLevelsForm()
    return render(request, 'lesson/assign_level.html', {'form': form})

@admin_access_only()
def AssignLevelsList(request):
    assign_levels = AssignLevels.objects.all()

    return render(request, 'lesson/assigned_list.html', {'assign_levels': assign_levels})