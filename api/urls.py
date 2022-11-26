from django.urls import path
from . views import *

urlpatterns = [
    path('<str:questions>/',GetQuestionsView.as_view(),name='questions'),
    path('<str:search>/',QuestionView.as_view(),name='search'),
    path('<str:advanced>/',AdvanceSearchView.as_view(),name='advanced'),
    path('<str:answer>/',QuestionsAnswer.as_view(),name='answer'),
]