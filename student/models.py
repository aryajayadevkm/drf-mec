from django.db import models
"""
An endpoint that serves student's details (roll, name, branch, year of joining) in JSON format.
"""
# Create your models here.


class Branch(models.Model):
    branch_name = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    year_of_joining = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)
