from importlib import import_module
from .models import BlogPost, MemberProfile, Order, Events, BlogPost, Comment
from .serializers import ContactSerializer, MemberSerializer,  EventSerializer, BlogPostSerializer, CommentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from app.permissions import IsOwner
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

import razorpay
from django.conf import settings
# Create your views here.

#View to show all members on home page
class MemberView(ListAPIView):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberSerializer

#View of Create profile page
class CreateProfileView(CreateAPIView):
    serializer_class = MemberSerializer

#View to see your profile
class YourProfileView(ListAPIView):
    serializer_class = MemberSerializer
    queryset = MemberProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset_main = self.queryset.filter(user=self.request.user)
        return queryset_main

#View to show all events on events page
class EventsView(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

#View to do search function
class SerachAPIView(ListAPIView):
    search_fields = ['name', 'company_name', 'category_field']
    filter_backends = (filters.SearchFilter,)
    queryset = MemberProfile.objects.all()
    serializer_class = MemberSerializer 

#View to contact page
class ContactView(CreateAPIView):
   serializer_class = ContactSerializer

#View to edit your profile
class UpdateProfileApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = "pk"
    def get_queryset(self):
        return MemberProfile.objects.all()
   
class DetailProfileApiView(RetrieveAPIView):
    serializer_class = MemberSerializer
    lookup_field = "pk"
    queryset = MemberProfile.objects.all()

class DetailEventApiView(RetrieveAPIView):
    serializer_class = EventSerializer
    lookup_field = "pk"
    queryset = Events.objects.all()



#View to Blogs
class BlogPostApiView(ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

#View to see all blogs
class CommentsView(CreateAPIView):
    serializer_class = CommentSerializer


#create payment
@api_view(['POST'])
def start_payment(request):
    amount = 20000
    name = request.user.username
    client = razorpay.Client(auth=(settings.PUBLIC_KEY, settings.SECRET_KEY))
    payment = client.order.create({"amount":int(amount)*100, "currency":"INR", "payment_capture":"1"})
    order = Order.objects.create(name=name, payment_id=payment['id'])    
    
    data = {
        "payment":payment, 
        "name":name
    }
    return Response(data)


