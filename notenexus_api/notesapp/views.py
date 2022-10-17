from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
# from rest_framework.permissions import isAuth

from .models import *
from .serializers import CreateNodeSerializer, NodeSerializer ,NoteSerializer
# Create your views here.

class CreateNodeView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Node.objects.all()
    serializer_class = CreateNodeSerializer

    def post(self, request):
        return Response({
            'data': self.create(request).data
        })

class NodeView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def get(self, request, pk=None):
        user = request.user
        data = self.queryset.filter(user=user).values()
        # right now we dont include user data on the actual notes and just on the node model. 
        
        if pk:
            return Response({
                'data': self.retrieve(request,pk).data
            })

        return Response({
            'data': data
        })

    def delete(self, request, pk=None):
        if pk:
            self.destroy(request, pk)
            return Response({
                'data': 'success'
            })
#  need to add edit view

class NoteView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, pk=None):
        if pk: 
            return Response({
                'data': self.retrieve(request,pk).data
            })
        return self.list(request)
    
    def post(self, request):
        return Response({
            "data": self.create(request).data
        })

    def put(self, request, pk=None):
        if pk:
            return Response ({
                'data': self.partial_update(request, pk).data
            }) 
    def delete(self, request, pk=None):
        if pk:
            return Response({
                'data': self.destroy(request, pk).data
                })
