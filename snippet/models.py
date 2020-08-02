from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50, default = '')
    subtitle = models.CharField(max_length = 100, default = '')
    introduction = models.TextField(null = True, default = '')
    content1 = models.TextField(null = True, verbose_name = 'Content', default = '')
    code = models.TextField(null = True, default = '')
    content2 = models.TextField(null = True, verbose_name = 'Content', default = '')
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})