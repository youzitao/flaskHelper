from django.shortcuts import render

# Create your views here.
from rest_framework import generics
import models
import serializers

class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

# class PostDetail(generics.RetrieveAPIView):
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer