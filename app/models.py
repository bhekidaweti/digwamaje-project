from django.db import models

# Create your models here.
class Services(models.Model):
    name_of_service = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='images/')  
    price = models.IntegerField()
    description = models.TextField()



    def __str__(self):
           return self.name_of_service
    
    @property
    def imageURL(self):
            try:
                url = self.image.url
            except:
                url = ''
            return url