from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.blog_home, name='blog'), #blog page
    path('<int:blog_id>/', views.detail, name='blog_detail'), #Individual blogs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

