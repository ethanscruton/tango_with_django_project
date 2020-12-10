from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    max_name_length = 128

    name = models.CharField(max_length=max_name_length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rango:show_category', 
                        kwargs={'category_name_slug': self.slug})

class Page(models.Model):
    max_title_length = 128

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=max_title_length)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('rango:show_category', 
                        kwargs={'category_name_slug': self.category.slug})

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_slug = models.SlugField(unique=True)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):
        self.user_slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('rango:profile', kwargs={'user_slug': self.user_slug})