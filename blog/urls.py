from django.urls import path
from .views import show_post

urlpatterns = [
    path("<slug:slug>", show_post, name="post_detail")
]