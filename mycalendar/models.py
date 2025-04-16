<<<<<<< HEAD
from django.db import models

# Create your models here.

class Appointments(models.Model):
    name = models.CharField(max_length= 200)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(max_length= 500, blank=True, null=True)
    status = models.CharField(max_length= 100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
=======
from django.db import models

# Create your models here.

class Appointments(models.Model):
    name = models.CharField(max_length= 200)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(max_length= 500, blank=True, null=True)
    status = models.CharField(max_length= 100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
>>>>>>> 72ce678392f09cfcd2104b67e6b794cbbfb143bb
      