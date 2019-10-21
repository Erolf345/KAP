from django.urls import path
from survey.views import *

urlpatterns = [
    path('', index, name='survey_list'),
    path('<int:id>/details', details, name='survey_details'),
    path('<int:id>/', question_content, name='question_content'),
    ]
