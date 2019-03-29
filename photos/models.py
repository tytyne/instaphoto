from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.
   
class User(models.Model):
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
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
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



    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        images = cls.objects.order_by('date_posted')
        return images
    
    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id = id)
        return image
    
    def __str__(self):
        return self.nam


class PhotosLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()        
   
  
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile_pic/', null = True)
    bio = models.TextField(max_length = 500, blank = True, null = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profiles(cls, query):
        profile = cls.objects.filter(user__username__icontains=query)
        return profile

    def __str__(self):
        return self.user.username
 
     
class Comment(models.Model):
    class Meta:
        db_table = "comments"
 
    path = ArrayField(models.IntegerField())
    image_id = models.ForeignKey(Image)
    user_id = models.ForeignKey(User)
    content = models.TextField('Comment')
    pub_date = models.DateTimeField('Date of comment')
 
    def __str__(self):
        return self.content[0:200]
 
    def get_offset(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return level
 
    def get_col(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return 12 - level