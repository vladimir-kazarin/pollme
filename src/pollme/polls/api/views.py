from rest_framework.views import APIView
from rest_framework.response import Response

#get models
from ..models import Question, Choice

#get serializers
from .serializers import (
    QuestionListSerializer
)

class QuestionListAPIView(APIView):

    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass

    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass
