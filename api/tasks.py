from celery import *

from api.models import *


def searchtask(query, apidata):
	if Questions.objects.filter(query=query).exists()==False:
		ques_db=Questions.objects.create(query=query, data=apidata)
		ques_db.save()

def answertask(question_id, apidata):
	if Answers.objects.filter(question_id=question_id).exists()==False:
		ans_db=Answers.objects.create(question_id=question_id, data=apidata)
		ans_db.save()
