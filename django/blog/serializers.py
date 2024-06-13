from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import PermissionDenied
from .models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'author' in validated_data:
            raise PermissionDenied(
                'You are not allowed to update the author field.',
                code='forbidden'
            )
        return super().update(instance, validated_data)
