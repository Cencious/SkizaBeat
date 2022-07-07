from django.contrib.auth.models import User
from rest_framework import serializers, validators

from rest_framework.authtoken.models import Token

from users import models

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            "password":{"write_only": True},
            "email":{
                "required": True,
                "allow_blank": False,
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(),"A user with that Email already exists"
                    )
                ]
            }
        }
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = User.objects.create(username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
        )

        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','profile_picture')
        extra_kwargs = {'password':{'write_only':True}}

    

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''for profile feed items'''

    class Meta:
        model=models.ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}






