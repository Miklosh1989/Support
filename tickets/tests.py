from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Answer
from .serializers import AnswerDetailSerializer


class AnswerTests(APITestCase):

    def setUp(self):
        Answer.objects.create(solutionOfProblem="Fucking Shit")
        self.one_answer = Answer.objects.create(solutionOfProblem="Goddamn")

    def test_answer_list(self):
        response = self.client.get(reverse('answerList'))
        print(response.data)

    def test_detail_answer_db(self):
        answer = Answer.objects.get(id= self.one_answer.id)
        print(answer)
        self.assertEqual(answer.solutionOfProblem, "Goddamn")

    def test_detail_answer(self):
        response = self.client.get(reverse('answerDetail', kwargs={"pk": self.one_answer.id}))
        serializer_data = AnswerDetailSerializer(self.one_answer).data
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response_data)