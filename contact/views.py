from rest_framework import generics
from .models import Contact, ContactInfo
from .serializers import ContactSerializer, ContactInfoSerializer


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()[:1]
    serializer_class = ContactInfoSerializer

