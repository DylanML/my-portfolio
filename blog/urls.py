from django.urls import path
from .views import blog, post_detail

app_name = 'blog'

urlpatterns = [
    path("", blog, name="blog"),
    path("<int:post_id>", post_detail, name="post_detail"),
]
