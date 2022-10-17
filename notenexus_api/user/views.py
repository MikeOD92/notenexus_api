from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, mixins
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status

# Create your views here.
class UserViews(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def post(self, request):
        data = request.data

        try:
            user = User.objects.create(
                username=data['email'],
                email = data['email'],
                password=make_password(data['password']),
            )
            serializer = UserSerializer

            return Response({
                'data': serializer(user).data
            })

        except:
            return Response({'message': "error"}, status=status.HTTP_400_BAD_REQUEST)

