from rest_framework import serializers

from ads.models import Ad, Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    ad = serializers.PrimaryKeyRelatedField(queryset=Ad.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_image = serializers.CharField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        exclude = ['description']


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.CharField(source='author.id', read_only=True)

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")
