from django.db import models


class ModelA(models.Model):
    pass


class ModelB(models.Model):
    a = models.ForeignKey(ModelA, null=True)
