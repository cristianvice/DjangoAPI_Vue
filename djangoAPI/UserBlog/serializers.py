from rest_framework import serializers
from UserBlog.models import Users, Blog

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('UserId', 'UserName')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=('BlogId', 'BlogName', 'BlogContent', 'BlogTag', 'PostDate', 'BlogUserId')
