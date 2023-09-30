"""
urls for the media 
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from media import views

router = DefaultRouter()
router.register('gallery', views.GalleryViewSet)
router.register('tags', views.TagViewSet)
router.register('image', views.ImageVIewSet)

app_name = 'media'

urlpatterns = [
    path('', include(router.urls)),
]