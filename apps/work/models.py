from django.db import models


class Work(models.Model):
    branding = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    link = models.CharField(max_length=202)
    image = models.ImageField(upload_to='work/')
    about = models.TextField()
    period = models.CharField(max_length=202)
    client = models.CharField(max_length=202)
    services = models.CharField(max_length=202)
    project = models.CharField(max_length=202)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ImageWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='work')
    image = models.ImageField(upload_to='work_images/')

    def __str__(self):
        return self.work.title
