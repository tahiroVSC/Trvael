from rest_framework import serializers

from apps.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News 
        fields = ('id', 'title', 'description', 
                  'image', 'created')