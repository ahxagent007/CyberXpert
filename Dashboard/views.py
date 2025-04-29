from django.shortcuts import render
from UserManager.decorators import login_access_only
from UserManager.models import UserAccount
from Lesson.models import AssignLevels, QuizPaper


@login_access_only()
def Dashboard(request):
    user = UserAccount.objects.get(id=request.user.id)
    level_count = AssignLevels.objects.filter(user=user).count()
    quic_taken_count = QuizPaper.objects.filter(user=user).count()
    lesson_done = QuizPaper.objects.filter(user=user).values('level').distinct().count()

    try:
        level_progress = int((lesson_done / level_count) * 100)
    except:
        level_progress  = 0

    data = {
        'level_progress': level_progress,
        'level_count': level_count,
        'quiz_count': str(quic_taken_count) + ' time'
    }
    return render(request=request, context=data, template_name='dashboard/dashboard.html')

@login_access_only()
def Message(request):
    data = {
        'msg': ''
    }
    return render(request=request, context=data, template_name='dashboard/message.html')