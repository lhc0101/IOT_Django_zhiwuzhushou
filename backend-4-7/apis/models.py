from django.db import models


# Create your models here.


class HistoryValue(models.Model):
    temperature = models.CharField(max_length=32)
    humidity = models.CharField(max_length=32)
    shidu = models.CharField(max_length=32)
    guangzhao = models.CharField(max_length=32)
    shebeiid = models.CharField(max_length=32)
    time = models.DateTimeField(auto_now=True)