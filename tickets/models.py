from django.db import models


class Answer(models.Model):
    solutionOfProblem = models.TextField(max_length=255, verbose_name='решение проблемы')
    dateOfAnswer = models.DateTimeField(auto_now_add=True, verbose_name='дата ответа')
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.solutionOfProblem


class Ticket(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    incident = models.TextField(max_length=255, verbose_name='инцидент')
    dateOfIncident = models.DateTimeField(auto_now=True, verbose_name='дата запроса')
    is_done = models.BooleanField(default=True, verbose_name='состояние запроса')
    answer = models.ForeignKey(Answer, verbose_name="ответ", on_delete=models.CASCADE, blank=True, null=True)
    parentTicket = models.ForeignKey('self', verbose_name="Родитель запроса", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.name


