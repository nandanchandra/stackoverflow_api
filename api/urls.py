from django.conf.urls import include,url

from . views import All_questions_View

urlpatterns = [
    url('questions/$',All_questions_View.as_view(),name='all_ques')

]