import api
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import *
from .myserializers import *

class getType(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class createForm(APIView):
    permission_classes = [AllowAny]    
    def post(self, request):
        uid = request.user.id
        data = request.data.copy()
        data['user'] = uid
        ser = FormSerializer(data = data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.error_messages)

class MyForm(APIView):
    def get(self, request):
        try:
            data = Form.objects.filter(user = request.user.id)
            ser = FormSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg':'id does not exist'})

class createQuestion(APIView):
    def post(self, request):
        ser = QuestionSerializer(data=request.data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.error_messages)

class editQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class createResponse(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResponseSerializer

class editUserResponse(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = UserResponse.objects.all()
    serializer_class = ResponseSerializer