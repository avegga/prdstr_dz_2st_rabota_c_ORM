from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=20)
    email = models.EmailField()
    born = models.CharField(max_length=4)
    department = models.ForeignKey(
        'company.Department',
        null=True,
        related_name='employees',
        on_delete=models.CASCADE

    )


    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    branch = models.ForeignKey(
        'company.Branch',
        null=True,
        related_name='departments',
        on_delete=models.SET_NULL
    )


class Branch(models.Model):
    short_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

