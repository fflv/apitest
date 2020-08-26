from rest_framework import serializers

from .models import Quiz, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    # def save(self, **kwargs):
    #     pass

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    # questions = QuestionSerializer(many=True, required=False)
    # quiz_end = serializers.DateField(format="%Y-%m-%d - %H:%M:%S")

    class Meta:
        model = Quiz
        fields = '__all__'


class ResultsSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'quiz_id': instance.question.question_quiz_id,
            'question_id': instance.question_id,
            'choice_id': instance.id,
            'q_text': instance.question.question_text,
            'choice_text': instance.text,
            'choice_right': instance.choice_right,
        }
