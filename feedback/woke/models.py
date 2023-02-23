from django.db import models

# Create your models here.

class db(models.Model):
    Name= models.CharField(max_length=30)
    Description = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="images/")
       
    def __str__(self):
        return self.Name
    
    