from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from django.utils.html import format_html


class BlogPost(models.Model):
    Blog_title = models.CharField(max_length=200)
    Title_url = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='Admin/blogimages/')
    content = RichTextField()

    def save(self, *args, **kwargs):
        if not self.Title_url:
            self.Title_url = slugify(self.Blog_title)

        super().save(*args, **kwargs)

    def clean(self):
        if not self.Title_url:
            raise ValidationError({'slug': 'Title URL cannot be empty.'})

        # Check if a blog with the same slug already exists
        existing_blog = BlogPost.objects.filter(
            Title_url=self.Title_url).exclude(id=self.id).first()
        if existing_blog:
            raise ValidationError(
                {'slug': 'A blog with this Title URL already exists.'})

    def __str__(self):
        return self.Blog_title
    
    class Meta:
        verbose_name = 'Blog' 
        verbose_name_plural = 'Blogs'


class ServicePost(models.Model):
    title = models.CharField(max_length=200)
    Title_Url = models.SlugField(unique=True, blank=True, null=True)
    Service_image = models.ImageField(upload_to='Admin/Serviceicons/')
    Service_icon = models.ImageField(upload_to='Admin/Serviceimages/')
    Description = models.CharField(max_length=255,)
    content = RichTextField() 

    def save(self, *args, **kwargs):
        if not self.Title_Url or self.title != self.Title_Url:
            self.Title_Url = slugify(self.title)

        super().save(*args, **kwargs)

    def clean(self):
        if not self.Title_Url:
            raise ValidationError({'Title_Url': 'Title URL cannot be empty.'})

        # Check if a service with the same slug already exists
        existing_service = ServicePost.objects.filter(
            Title_Url=self.Title_Url).exclude(id=self.id).first()
        if existing_service:
            raise ValidationError(
                {'Title_Url': 'A service with this Title URL already exists.'})

        # Validate Description length
        max_char_count = 255
        if len(self.Description) > max_char_count:
            raise ValidationError({'Description': f'Description should not exceed {max_char_count} characters.'})
            
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service' 
        verbose_name_plural = 'Services'
  

def gallery_image_path(instance, filename):
    cleaned_name = slugify(instance.gallery.Gallery_Title)
    service_name = slugify(instance.gallery.service.title)
    return f'Admin/GalleryImages/{service_name}/{cleaned_name}/{filename}'

class Gallery(models.Model):
    service = models.ForeignKey(ServicePost, on_delete=models.CASCADE)
    Gallery_Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Gallery_Title
    
    class Meta:
        unique_together = ('service', 'Gallery_Title')
        verbose_name = 'Gallery' 
        verbose_name_plural = 'Gallery'
  
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Admin/GalleryImages/', max_length=100)

    def __str__(self):
        return format_html('<img src="{}" width="50" height="50" />', self.image.url)

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    interested_in = models.ForeignKey(ServicePost, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name