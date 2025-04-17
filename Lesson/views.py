from django.shortcuts import render
from .models import Questions, Level, AssignLevels
from UserManager.decorators import login_access_only
from UserManager.models import UserAccount


@login_access_only()
def Quiz(request, level_no):
    if request.method == 'GET':
        question_list = Questions.objects.filter(level_number=level_no)
        level = Level.objects.get(number=level_no)
        data = {
            'question_list': question_list,
            'level': level.name,
            'level_description': level.description,
            'level_no': level_no
        }
        return render(request=request, template_name='lesson/quiz.html', context=data)
    elif request.method == 'POST':
        data = request.POST
        print(data)
        
        return Redirect('Dashboard:Message')

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