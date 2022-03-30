from rest_framework import serializers
from .models import Profiles
import re
from rest_framework.exceptions import ValidationError
from posts.serializers import PostSerializer
from django.contrib.auth.models import User
from posts.models import Posts
from django.shortcuts import get_object_or_404


class ProfileSerializerV1(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post = PostSerializer(write_only=True, required=False)
    user = serializers.IntegerField(write_only=True)

    class Meta:
        model = Profiles
        fields = "__all__"

    def validate_phone_number(self, value):
        phone_number_pattern = re.compile("^09\d{9}$")
        if phone_number_pattern.match(value):
            return value

        raise ValidationError('your phone number pattern is not correct')

    def create(self, validated_data):
        if 'post' in validated_data:
            user = validated_data.pop('user')
            user = get_object_or_404(User, pk=user)
            post = validated_data.pop('post')
            profile = Profiles.objects.create(user=user, **validated_data)
            my_post = Posts.objects.create(**post, author=profile)
        else:
            user = validated_data.pop('user')
            user = get_object_or_404(User, pk=user)
            profile = Profiles.objects.create(user=user, **validated_data)

        return profile


class ProfileSerializerV2(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post = PostSerializer(write_only=True, required=False)
    user = serializers.IntegerField(write_only=True)

    class Meta:
        model = Profiles
        fields = ['first_name', 'posts', 'post', 'user']

    def create(self, validated_data):
        if 'post' in validated_data:
            user = validated_data.pop('user')
            user = get_object_or_404(User, pk=user)
            post = validated_data.pop('post')
            profile = Profiles.objects.create(user=user, **validated_data)
            my_post = Posts.objects.create(**post, author=profile)
        else:
            user = validated_data.pop('user')
            user = get_object_or_404(User, pk=user)
            profile = Profiles.objects.create(user=user, **validated_data)

        return profile
