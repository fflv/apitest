from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    quiz_created = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=100)
    quiz_start = models.DateTimeField(auto_now_add=True, editable=False)
    quiz_end = models.DateTimeField(blank=True, null=True)
    quiz_description = models.TextField()


class Question(models.Model):
    QTYPE = (
        (1, 'text'),
        (2, 'single_choice'),
        (3, 'multi_choice'),
    )
    question_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_type = models.PositiveSmallIntegerField(choices=QTYPE, default=1)
    question_text = models.CharField(max_length=200)
    question_options = models.CharField(max_length=100, blank=True)
    question_answer = models.CharField(max_length=100, blank=True)


class Choice(models.Model):
    text = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.PositiveSmallIntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_right = models.BooleanField(default=False)

    class Meta:
        unique_together = ('question', 'user')





