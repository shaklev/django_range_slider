from django.db import models

# Create your models here.


class TestModel(models.Model):
    range_field = models.CharField(max_length=200)
    name_range_field = models.CharField(max_length=200)
    label_field = models.CharField(max_length=230)
