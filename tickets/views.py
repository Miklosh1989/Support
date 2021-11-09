from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class TicketListView(generics.ListAPIView):

    queryset = Ticket.objects.filter(is_done = False)
    serializer_class = TicketListSerializer


class TicketDetailView(APIView):

    def get(self, request, pk):
        ticket = Ticket.objects.get(id=pk, is_done = False)
        serializer = TicketDetailSerializer(ticket)
        return Response(serializer.data)


class AnswerListView(generics.ListAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer


class AnswerDetailView(APIView):

    def get(self, request, pk):
        answer = Answer.objects.get(id=pk)
        serializer = AnswerDetailSerializer(answer)
        return Response(serializer.data)


class TicketCreateView(generics.CreateAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer


class TicketUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateSerializer
