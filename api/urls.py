from django.conf.urls import url

from . views import *

urlpatterns = [
    url('questions/$',All_questions_View.as_view(),name='all_ques'),
    url('search/$',QuestionView.as_view(),name='search'),
    url('searchAd/$',AdvanceSearchView.as_view(),name='searchAd'),
    url('answer/$',QuestionsAnswer.as_view(),name='answer'),

]