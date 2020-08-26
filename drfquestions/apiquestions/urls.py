from django.urls import path
from .views import QuizesList, QuizDetail, QuestionsList, CreateChoice, ResultsList, QuizesActiveList

urlpatterns = [
    path("quiz/", QuizesList.as_view(), name="quiz_list"),
    path("quiz/<int:pk>/", QuizDetail.as_view(), name="quiz_detail"),
    path("quiz/<int:pk>/questions/", QuestionsList.as_view(), name="questions_list"),
    path("quiz/<int:pk>/questions/<int:question_pk>/choice/", CreateChoice.as_view(), name="choice_create"),
    path("results/<int:pk>/", ResultsList.as_view(), name="results"),
    path("activequizes/", QuizesActiveList.as_view(), name="activequixes"),
]

