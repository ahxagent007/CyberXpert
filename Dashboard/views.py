from django.shortcuts import render


def Dashboard(request):
    data = {
        'level_progress': 50,
        'level_count': 3,
        'quiz_count': 2
    }
    return render(request=request, context=data, template_name='dashboard/dashboard.html')

def Message(request):
    NotImplemented