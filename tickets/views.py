from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class TicketListView(generics.ListAPIView):

    queryset = Ticket.objects.filter(is_done = False)
    serializer_class = TicketListSerializer
    permission_classes = [permissions.IsAuthenticated]

class TicketDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        ticket = Ticket.objects.get(id=pk, is_done = False)
        serializer = TicketDetailSerializer(ticket)
        return Response(serializer.data)


class AnswerListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer


class AnswerDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        answer = Answer.objects.get(id=pk)
        serializer = AnswerDetailSerializer(answer)
        return Response(serializer.data)


class TicketCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [permissions.IsAdminUser]


class TicketUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateSerializer
    permission_classes = [permissions.IsAdminUser]