from rest_framework import serializers
from .models import Student, Branch


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('branch_code', 'branch_name')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name','branch', 'roll_no', 'year_of_joining')


class StudentDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField()
    branch = serializers.CharField(source='branch.branch_name')

    class Meta:
        model = Student
        fields = ('full_name', 'roll_no', 'branch', 'year_of_joining')


