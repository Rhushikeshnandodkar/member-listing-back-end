
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
#categories for member model
class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

#member profile model
class MemberProfile(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_details = models.TextField()
    profile_image = models.ImageField(upload_to="images")
    address = models.TextField()
    contact = models.CharField(max_length=100)
    category_field = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#blogs category model
class BlogCategory(models.Model):
    cat_title = models.CharField(max_length=120)
    def __str__(self):
        return self.cat_title

#blogs model
class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(BlogCategory, related_name='blog_category', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="image", blank=True)
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

#comments model
class Comment(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)

#events model
class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    agenda = models.TextField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    start_day = models.DateField(blank=True, null=True)
    end_day = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50)
    event_image = models.ImageField(upload_to="images")
    def __str__(self):
        return self.title

#contact page model
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    content = models.TextField()
    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=120)
    payment_id = models.CharField(max_length=120)
    order_date = models.DateTimeField(auto_now=True)



