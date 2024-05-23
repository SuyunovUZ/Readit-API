from django.urls import path
from .views import ContactAPIView, ContactInfoAPIView

urlpatterns = [
    path('', ContactAPIView.as_view(), name='contact'),
    path('info/', ContactInfoAPIView.as_view(), name='contact-information')
]
