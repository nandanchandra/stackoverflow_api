from rest_framework import serializers
from api.models import Questions,Answers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        depth = 2
        fields = '__all__'

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        depth = 2
        fields = '__all__'
