import logging
from celery import task
from api.models import *

logger = logging.getLogger(__name__)

@task(name="searchtask")
def searchtask(query, apidata):
	if Questions.objects.filter(query=query).exists()==False:
		ques_db=Questions.objects.create(query=query, data=apidata)
		ques_db.save()
		logger.info("Data Saved In DB")

@task(name="answertask")
def answertask(question_id, apidata):
	if Answers.objects.filter(question_id=question_id).exists()==False:
		ans_db=Answers.objects.create(question_id=question_id, data=apidata)
		ans_db.save()
		logger.info("Answer Saved In DB")