from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}, {self.city}, {self.address}"

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}, {self.salary}, {self.company}"