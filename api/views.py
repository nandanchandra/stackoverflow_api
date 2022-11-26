from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle

from .utils import GetStackExchange

from api.models import Questions,Answers
from api.serializers import QuestionSerializer,AnswersSerializer

class GetQuestionsView(APIView):


	def get(self,request,*args,**kwargs):
		page=self.request.GET.get("page")
		all_ques = GetStackExchange()
		all_ques = all_ques.get_all_questions(page)
		return Response(all_ques,status=status.HTTP_200_OK)


class QuestionView(APIView):

	throttle_classes = [AnonRateThrottle]


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

class AdvanceSearchView(APIView):

	throttle_classes = [AnonRateThrottle]

	def get(self,request,*args,**kwargs):
		page=self.request.GET.get("page")
		query=self.request.GET.get("query")
		qs = Questions.objects.filter(query=query)
		
		if qs.exists():
			objects = qs.first()
			serialized_data = QuestionSerializer(objects)
			data = serialized_data.data['data']
			return Response(data,status=status.HTTP_200_OK)
		
		advanceresult = GetStackExchange()
		advanceresult = advanceresult.advanceSearch(query,page)
		return Response(advanceresult,status=status.HTTP_200_OK)


class QuestionsAnswer(APIView):
	def get(self,request,*args,**kwargs):
		question_id = self.request.GET.get("quesid",None)
		
		if question_id is None:
			return Response({"error":"Question Id is required"},status=400)

		qs = Answers.objects.filter(question_id=question_id)

		if qs.exists():
			objects = qs.first()
			serialized_data = AnswersSerializer(objects)
			data = serialized_data.data['data']
			return Response(data,status=status.HTTP_200_OK)

		res = GetStackExchange()
		res = res.answer(question_id)
		return Response(res,status=status.HTTP_200_OK)