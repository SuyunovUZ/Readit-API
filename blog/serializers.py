from rest_framework import serializers
from .models import (Author,
                     About,
                     Category,
                     Comment,
                     Post,
                     HappyClients,
                     Tag)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'tags', 'author', 'category', 'description', 'comment_set', 'created_at',
                  'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class HappyClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyClients
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
