from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField(
        'Name', blank=False, null= False,max_length=14, db_index=True
    )
    body = models.CharField(
        'body', blank=True, null=True,max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    like = models.PositiveIntegerField(
        "like", default=0, null=True, blank=True
    )
    image = CloudinaryField (
        "image", blank=True, 
    )
    
    def __str__(self):
        return self.name
    