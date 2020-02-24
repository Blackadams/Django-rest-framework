from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError
    )
from .models import Post , Account


User = get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = ['f_name','occupation']


class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account

        fields = [

            'username',
            'email',
            'password',
            'password2',
        ]

        extra_kwargs = {'password':{'write_only': True}}



    def save(self):

        account = Account(
                email=self.validated_data['email'],
                username=self.validated_data['username'],


        )

        password = self.validated_data['password'],
        password2 = self.validated_data['password2'],

        if password != password2:
            raise serializers.ValidationError({'password': 'passwords must match'})
        account.set_password(password)
        account.save()

        return account







#
# class UserLoginSerializer(serializers.ModelSerializer):
#     token = CharField(allow_blank=True, read_only=True)
#     username = CharField()
#     email = EmailField(label='Email Address')
#
#     class Meta:
#         model = User
#
#         fields = [
#
#             'username',
#             'email',
#             'password',
#             'token',
#         ]
#
#         extra_kwargs = {'password':{'write_only': True}}
