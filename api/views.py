from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import GetStackExchange

class All_questions_View(APIView):

	def get(self,request,*args,**kwargs):
		page=self.request.query_params.get("page")
		all_ques = GetStackExchange()
		all_ques = all_ques.get_all_questions(page)
		return Response(all_ques,status=status.HTTP_200_OK)