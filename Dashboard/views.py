from django.shortcuts import render

# Create your views here.
def Dashboard(request):
    return render(request=request, context={}, template_name='dashboard/dashboard.html')