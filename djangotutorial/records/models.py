from django.db import models


class Record(models.Model):
    enregistre = models.CharField(max_length=200)

    def __str__(self):
        return self.enregistre