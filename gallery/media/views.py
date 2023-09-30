"""
views for the media
"""

from rest_framework import (viewsets, mixins, status)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from media.models import (GalleryModel, TagModel, ImageModel)
from media.serialiizer import (
    TagModelSerializer,
    ImageModelSerializer,
    GalleryModelSerializer,
)


class GalleryViewSet(viewsets.ModelViewSet):
    """view for manage recipe API"""
    serializer_class = GalleryModelSerializer
    queryset = GalleryModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """retrieve query set for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """return the serializer class for request"""
        if self.action=='upload_image':
            return ImageModelSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """create a new gallary"""
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """function for uploading image to imagemodel"""
        image = self.get_object()
        serializer = self.get_serializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagViewSet(viewsets.ModelViewSet):
    """manage tags in the database"""
    serializer_class = TagModelSerializer
    queryset = TagModel.objects.all()
    

class ImageVIewSet(viewsets.ModelViewSet):
    """manageimage Database"""
    serializer_class = ImageModelSerializer
    queryset = ImageModel.objects.all()

