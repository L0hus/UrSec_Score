from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    name = models.CharField(max_length=60, blank=False)


class Ugroup(models.Model):
    name = models.CharField(max_length=10, blank=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500, blank=True)
    faculty = models.ForeignKey(Faculty, verbose_name="Факультет", on_delete=models.CASCADE)
    group = models.ForeignKey(Ugroup, verbose_name="Группа", on_delete=models.CASCADE)
