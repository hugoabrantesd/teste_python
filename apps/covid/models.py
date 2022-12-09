from django.db import models

# Create your models here.


class Covid(models.Model):

    uid = models.IntegerField()
    uf = models.CharField(max_length=2)
    state = models.CharField(max_length=20)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    suspects = models.IntegerField()
    refuses = models.IntegerField()
    datetime = models.CharField(max_length=40)
