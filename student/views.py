from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from student.serializers import StudentSerializer


class StudentList(APIView):

    def get(self, request, format=None):
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)



