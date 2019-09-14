from django.db import models

# Create your models here.
class User(models.Model):
    # The First Name Field
    first_name = models.CharField(max_length=128)
    # Last Name Field
    last_name = models.CharField(max_length=128)
    # Email Field & Unqiue to make sure each email is unique
    email = models.EmailField(max_length=254,unique=True)
