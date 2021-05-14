from rest_framework import serializers
from .models import Post,PostComment,PostLike
from userProfile.serializers import UserProfileSerializers

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def get_user(self,obj):
        user = obj.user.userProfile
        serializer = UserProfileSerializers(user, many=False)
        return serializer.data


class PostCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PostComment
        field = '__all__'
    
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializers(user, many=False)
        return serializer.data


class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PostLike
        field = '__all__'
    
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializers(user, many=False)
        return serializer.data
