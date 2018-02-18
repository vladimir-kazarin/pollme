
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from ..models import Question, Choice

class QuestionListSerializer(ModelSerializer):

    choices = SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'id',
            'text',
            'pub_date',
            'choices',
        ]

    def get_choices(self, obj):
        choice_qs = obj.choice_set.all()
        return ChoiceSerializer(choice_qs, many=True).data

class ChoiceSerializer(ModelSerializer):

    class Meta:
        model = Choice
        fields = [
            'choice_text',
            'votes'
        ]
