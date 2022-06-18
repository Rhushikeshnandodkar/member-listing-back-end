from app.views import  MemberView, CreateProfileView,DetailEventApiView, DetailProfileApiView, start_payment, YourProfileView, EventsView, SerachAPIView, UpdateProfileApiView,  ContactView, BlogPostApiView, CommentsView
from django.urls import path
from . import views

urlpatterns = [
       
       path('', MemberView.as_view()),  #homepage url
       path('createprofile', CreateProfileView.as_view()),  #createprofile url
       path('yourprofile/', YourProfileView.as_view(),),    #seeprofile url
       path('events/', EventsView.as_view()),    #eventspage url
       path('update/<int:pk>', UpdateProfileApiView.as_view(), ), #update profile
       path('detail/<int:pk>', DetailProfileApiView.as_view(), ), #update profile
       path('contact', ContactView.as_view()),  #contactpage url
       path('filters', SerachAPIView.as_view()), #search url
       path('blogs', BlogPostApiView.as_view()), #blogs url
       path('commentsapi', CommentsView.as_view()) ,  #comments url
       path('startpayment', views.start_payment),   #Payment url
       path('eventsdetail/<int:pk>', DetailEventApiView.as_view())
]
