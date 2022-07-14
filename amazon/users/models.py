from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profilePicture = models.FileField(upload_to="registration/static/images")

    def __str__(self):
        return f"{self.username}"
