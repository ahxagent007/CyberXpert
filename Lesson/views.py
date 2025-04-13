from django.shortcuts import render




def Quiz(request):
    data = {}
    return render(request=request, template_name='lesson/single_question.html', context=data)
