from django.db import models


class ContactMe(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=202)
    location = models.CharField(max_length=202)

    def __str__(self):
        return self.phone_number


class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    phone_number = models.CharField(max_length=202)
    message = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
