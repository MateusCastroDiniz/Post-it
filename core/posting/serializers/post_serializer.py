from rest_framework import serializers
from core.posting.models import Post, PostFile
from .comment_serializer import CommentSerializer
from .post_file_serializer import PostFileSerializer
from .user_serializer import UserSerializer
from .like_serializer import LikeSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    files = PostFileSerializer(read_only=True, many=True)
    likes = LikeSerializer(read_only=True, many=True)
    author_username = serializers.ReadOnlyField(source='author.username')
    author_profile_picture = serializers.ReadOnlyField(source='author.profile_picture.profile_picture.url')

    class Meta:
        model = Post
        fields = [
            'id',
            'text_content',
            'created_on',
            'updated_on',
            'author_username',
            'files',
            'slug',
            'comments',
            'author_profile_picture',
            'likes'
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text_content = validated_data.get('text_content', instance.text_content)
        instance.save()
        return instance


