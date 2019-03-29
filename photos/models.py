from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
   
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']        
class tags(models.Model):
    name = models.CharField(max_length =30,blank =True )

    def __str__(self):
        return self.name
from tinymce.models import HTMLField
class Image(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)    
    image_image = models.ImageField(upload_to = 'images/',blank=True)
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos
   
    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos    
    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos        

class PhotosLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()        
   
  
   
     
