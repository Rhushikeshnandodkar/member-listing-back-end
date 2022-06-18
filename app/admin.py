from django.contrib import admin
from .models import MemberProfile, Category, Order, Events, Contact, Comment, BlogPost, BlogCategory
# Register your models here.
admin.site.register(MemberProfile)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(BlogPost)
admin.site.register(Order)
admin.site.register(BlogCategory)
admin.site.register(Events)
admin.site.register(Contact)
