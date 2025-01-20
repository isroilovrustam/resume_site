from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class About(BaseModel):
    full_name = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    username = models.CharField(max_length=202)
    telegram = models.CharField(max_length=202)
    instagram = models.CharField(max_length=202)
    linkedin = models.CharField(max_length=202)
    github = models.CharField(max_length=202)
    facebook = models.CharField(max_length=202)
    twitter = models.CharField(max_length=202)
    description = models.TextField()

    def __str__(self):
        return self.full_name


class Experience(BaseModel):
    year = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    job = models.CharField(max_length=202)
    description = models.TextField()

    def __str__(self):
        return self.title


class Education(BaseModel):
    year = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    description = models.TextField()

    def __str__(self):
        return self.title
