from django.conf.urls import url

from . views import *

urlpatterns = [
    url('questions/$',All_questions_View.as_view(),name='all_ques'),
    url('search/$',Query_ques_View.as_view(),name='search'),

]