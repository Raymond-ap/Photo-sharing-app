from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
   

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    preview_text = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='image/')
    tag = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    slug =  models.SlugField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        global str
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Photo.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Photo.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)
    

"""[summary]
height_field=None, width_field=None, max_length=None
"""