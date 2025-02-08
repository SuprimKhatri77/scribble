from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(unique=True,blank=True,null=True)


    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Note.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Note(models.Model) :
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True,max_length=200,null=True,blank=True)
    categories = models.ManyToManyField(Category,blank=True)


    def __str__(self):
        return f'{self.author.username} - {self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Note.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
    