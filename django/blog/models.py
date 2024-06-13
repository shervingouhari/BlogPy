from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator as FEV
from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):
    avatar = models.FileField(upload_to='user/', validators=[FEV(['jpg', 'png'])], blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    
    def __str__(self):
        return self.username


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title[:30]

    title = models.CharField(max_length=128)
    cover = models.FileField(upload_to='category/', validators=[FEV(['jpg', 'png'])])


class Article(models.Model):
    class Meta:
        ordering = ['-updated']
        
    def __str__(self):
        return self.title[:30]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    cover = models.FileField(upload_to='article/', validators=[FEV(['jpg', 'png'])])
    content = CKEditor5Field()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    promoted = models.BooleanField(default=False)
