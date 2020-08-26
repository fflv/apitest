from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from datetime import datetime

from .models import Quiz, Question, Choice
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer, ResultsSerializer


class QuizesList(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionsList(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.filter(question_quiz_id=self.kwargs["pk"])
        return queryset


class CreateChoice(APIView):
    def post(self, request, pk, question_pk):
        text = request.data.get("text")
        user = request.data.get("user")
        question = Question.objects.get(id=question_pk)

        chooice_right = question.question_answer == text

        data = {
            "text": text,
            "user": user,
            "question": question_pk,
            "choice_right": chooice_right,
        }

        serializer = ChoiceSerializer(data=data)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultsList(APIView):
    def get(self, request, pk):
        choices = Choice.objects.filter(user=pk)

        # data = {pk: {}}
        # for choice in choices:
        #     # print(choice.id, choice.question_id, choice.question.question_text, choice.question.question_quiz_id)
        #     data[pk]
        #     data["results"][choice.question.question_quiz_id] = {
        #         choice.question_id: {
        #             "choice_id": choice.id,
        #             "question text": choice.question.question_text,
        #             "choice_text": choice.text,
        #             }
        #     }
        serializer = ResultsSerializer(choices, many=True).data
        # serializer = ResultsSerializer(choices, many=True).data
        return Response(serializer)
        # return JsonResponse(data)

        # serializer = ResultsSerializer(instance=choices).data
        # print(serializer)

        # return Response(serializer.data, status=status.HTTP_200_OK)


class QuizesActiveList(APIView):
    def get(self, request):
        quizes = Quiz.objects.filter(quiz_end__lte=datetime.today())
        serializer = QuizSerializer(quizes, many=True).data
        return Response(serializer)
