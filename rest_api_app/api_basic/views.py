from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import  JSONParser
from .models import User, ActivityPeriod
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
# @csrf_exempt
# def user_list(request):
#     """
#     List all  user, or create a new User.
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         print(serializer.data)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ActivityDetails(APIView):
#
#     def get_object(self, id):
#         try:
#             return User.objects.get(id=id)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     def get(self, request, id):
#         user = self.get_object(id)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#
#
#     def put(self, request,id):
#         user = self.get_object(id)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         user = self.get_object(id)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)