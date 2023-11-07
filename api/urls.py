from .views import dns_info
# import rest_framework format suffix patterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

urlpatterns = [
    path('dns_info/', dns_info, name='dns_info'),
]

urlpatterns = format_suffix_patterns(urlpatterns)