from django.urls import path
from .views import *

urlpatterns=[
    path('quiz/<int:level_no>', Quiz, name='Quiz'),
    path('quiz/result', QuizResult, name='QuizResult'),
    path('list', LessonList, name='LessonList'),
    path('assign', AssignLevelsView, name='AssignLevelsView'),
    path('assigned/list', AssignLevelsList, name='AssignLevelsList'),

]