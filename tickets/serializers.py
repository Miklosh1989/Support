from rest_framework import serializers
from rest_framework.response import Response

from .models import *


class TicketListSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = ("name", "incident", "answer")


class TicketDetailSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = ("name", "incident", "answer", "dateOfIncident")


class AnswerListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Answer
        fields = "__all__"


class AnswerDetailSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = "__all__"


class TicketCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ("name", "incident", "answer", "dateOfIncident")


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"


class TicketUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('is_done', )

