from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('projects/',views.pro, name='project'), #Projects page
    path('projects/<int:project_id>/', views.detail, name='detail'), #Individual Projects page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

