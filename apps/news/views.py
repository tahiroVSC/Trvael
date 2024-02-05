from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from apps.news.models import News
from apps.news.serializers import NewsSerializer
from apps.news.permissions import NewsPermission

# Create your views here.
class NewsAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (NewsPermission(), )
        return (AllowAny(), )