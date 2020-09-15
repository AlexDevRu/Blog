from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='avatars/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blogs:users:user_detail', kwargs={'slug': self.user.username})
