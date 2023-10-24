from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField( max_length=50)
    subj = models.CharField( max_length=50)