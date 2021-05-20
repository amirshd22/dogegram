from rest_framework import serializers
from .models import Tweets,TweetComment,UpVoteTweet
from userProfile.serializers import UserProfileSerializers

class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = '__all__'

    def get_user(self,obj):
        user = obj.user.userProfile
        serializer = UserProfileSerializers(user, many=False)
        return serializer.data


class TweetCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TweetComment
        field = '__all__'
    
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializers(user, many=False)
        return serializer.data



class TweetLikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UpVoteTweet
        field = '__all__'
    
    def get_user(self, obj):
        user = obj.user.userprofile
        serializer = UserProfileSerializers(user, many=False)
        return serializer.data
