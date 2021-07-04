from django.db.models import JSONField
from django.db import models

class Questions(models.Model):
	query = models.CharField(max_length=1000)
	data = JSONField(null=True)

	def __str__(self):
		return self.query

class Answers(models.Model):
	question_id = models.IntegerField()
	ques_data = JSONField(null=True)
	
	def __str__(self):
		return str(self.question_id)

