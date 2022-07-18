from django.db import models


class TestTable(models.Model):
    name = models.CharField(max_length=128, null=True)
    number = models.IntegerField(default=0)
    description = models.TextField()

# Create your models here.
