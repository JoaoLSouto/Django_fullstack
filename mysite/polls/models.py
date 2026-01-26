from django.db import models


class Question(models.Model):
    question_text = models.CharField("Texto da questão", max_length=200)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=True)
    x = models.TextField()

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"
