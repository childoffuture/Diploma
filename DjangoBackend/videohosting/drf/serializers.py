from rest_framework import serializers

from videoportal.models import Video


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['pk', 'name', 'id_author', 'id_category', 'created',
                  'description', 'likes', 'dislikes', 'video']
