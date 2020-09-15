from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='tags/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:tag', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='posts/')
    text = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post', kwargs={'slug': self.slug})
