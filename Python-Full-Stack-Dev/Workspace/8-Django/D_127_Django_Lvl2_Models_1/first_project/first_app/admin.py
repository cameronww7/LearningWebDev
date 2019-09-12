from django.contrib import admin
from .models import Topic,Webpage,AccessRecord # Import your models
# Register your models here.
admin.site.register(Topic)          # Declare Models
admin.site.register(Webpage)        # Declare Models
admin.site.register(AccessRecord)   # Declare Models
