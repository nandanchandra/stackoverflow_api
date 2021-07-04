from django.conf.urls import url

from . views import *

urlpatterns = [
    url('questions/$',GetQuestionsView.as_view(),name='questions'),
    url('search/$',QuestionView.as_view(),name='search'),
    url('searchAd/$',AdvanceSearchView.as_view(),name='searchAd'),
    url('answer/$',QuestionsAnswer.as_view(),name='answer'),

]