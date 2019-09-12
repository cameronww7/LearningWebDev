from django.db import models
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# CREATE SOME TEST DATA WITH SOME SHELL COMMANDS:

# python manage.py shell

# from first_app.models import Topic
# print(Topic.objects.all())
# t = Topic(top_name="Social Network")
# t.save()
# print(Topic.objects.all())
# quit()

# Create your models here.

# Instance of Topic
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

# Insance of Webpage
class Webpage(models.Model):
    # these are the columns in the webpage instance
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

# Instance of AccessRecord
class AccessRecord(models.Model):
    # More columns
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
