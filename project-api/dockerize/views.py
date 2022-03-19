from django.shortcuts import render
from rest_framework import generics
from .serializer import DockerizeSerializer
from .models import Dockerize
# Create your views here.

# class DockerizeList(generics.ListAPIView):
#   queryset = Dockerize.objects.all()
#   serializer_class = DockerizeSerializer

class DockerizeList(generics.ListCreateAPIView):
  queryset = Dockerize.objects.all()
  serializer_class = DockerizeSerializer


class DockerizeDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dockerize.objects.all()
  serializer_class = DockerizeSerializer


# class DockerizeUpdate(generics.RetrieveUpdateAPIView):
#   queryset = Dockerize.objects.all()
#   serializer_class = DockerizeSerializer



# class DockerizeDelete(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Dockerize.objects.all()
#   serializer_class = DockerizeSerializer