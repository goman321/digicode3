from django.urls import path
from .views import index, clear_cache, about_us, contact


urlpatterns = [
    path('clear_cache', clear_cache),
    path('', index),
    path('about', about_us),
    path('contact', contact)
]
