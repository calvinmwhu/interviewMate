from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    content = models.TextField(max_length=1024)

    def __unicode__(self):
        return self.title

#
# class QuestionContent(models.Model):
# question = models.OneToOneField(Question, primary_key=True)
#     content = models.TextField(max_length=1024)
#
#     def __unicode__(self):
#         return self.content

#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     picture = models.ImageField(upload_to='profile', blank=True)
#
#     def __unicode__(self):
#         return self.user.username
#
#     def __str__(self):
#         return self.user.username




