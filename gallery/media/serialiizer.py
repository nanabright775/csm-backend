from rest_framework import serializers
from media.models import (
    TagModel,
    GalleryModel,
    ImageModel,
)

class TagModelSerializer(serializers.ModelSerializer):
    """seializer for tags"""

    class Meta:
        model = TagModel
        fields = ['id', 'tagname', 'description']
        read_only_fields = ['id']
        
        
class  GalleryModelSerializer(serializers.ModelSerializer):
    """serializers for gallery"""
    tag = TagModelSerializer
    
    class Meta:
        model = GalleryModel
        fields = ['tags', 'title', 'description', 'date_created']  
        
class ImageSerializer(serializers.ModelSerializer):
    """serializer for uploading images to imagemodels"""
    class Meta:
        model = ImageModel
        fields =['id', 'image', ]
        read_only_fields=['id']
        extra_kwargs = {'image': {'required': 'True'}}

class ImageModelSerializer(serializers.ModelSerializer):
    """serielizers for image fields"""
    gallery = GalleryModelSerializer
    image = ImageSerializer
    class Meta:
        model = ImageModel
        fields = ['title', 'description', 'date_created', 'gallery', 'image']