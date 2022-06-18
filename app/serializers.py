from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogCategory, Category, MemberProfile, Events, Contact, BlogPost, Comment


#Members model serializer


class MemberSerializer(serializers.ModelSerializer):    
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MemberProfile
        fields = '__all__'
    
#Events model serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

#Contact model serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'

#Blog model serializer
class BlogPostSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = '__all__'

#Comments model serializer
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'


