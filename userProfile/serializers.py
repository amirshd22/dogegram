from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User



class UserProfileSerializers(serializers.ModelSerializer):
    profilePic = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UserProfile
        fields = "__all__"

    def get_profilePic(self, obj):
        try:
            pc = 'static' + obj.profilePic.url
        except:
            pc = None
        return pc
    
class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'profile', 'username', 'is_superuser', 'is_staff']

    def get_profile(self, obj):
        profile = obj.userprofile
        serializer = UserProfileSerializers(profile, many=False)
        return serializer.data