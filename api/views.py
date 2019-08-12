from django.shortcuts import render

from rest_framework import  generics
from .models import Escalas
from .serializers import EscalasSerializers

# Create your views here.

class EscalasList(generics.ListCreateAPIView):

    queryset = Escalas.objects.all()

    serializer_class = EscalasSerializers