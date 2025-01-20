from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=202)
    icon = models.CharField(max_length=202)
    description = models.TextField()

    def __str__(self):
        return self.title
