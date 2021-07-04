from django.db.models import query
from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import GetStackExchange

from api.models import Questions
from api.serializers import QuestionSerializer

class All_questions_View(APIView):

	def get(self,request,*args,**kwargs):
		page=self.request.query_params.get("page")
		all_ques = GetStackExchange()
		all_ques = all_ques.get_all_questions(page)
		return Response(all_ques,status=status.HTTP_200_OK)


class Query_ques_View(APIView):

	def get(self,request,*args,**kwargs):
		page = self.request.GET.get("page")
		query = self.request.GET.get("query")
		sort =self.request.GET.get("sort")
		order =self.request.GET.get("order")

		qs = Questions.objects.filter(query=query)
		if qs.exists():
			qb = qs.first()
			serialized_data = QuestionSerializer(qb)
			data = serialized_data.data['data']
			return Response(data,status=status.HTTP_200_OK)
		qr = GetStackExchange()
		qr = qr.search(page,query,order,sort)
		return Response(qr,status=status.HTTP_200_OK)


