from django.contrib.auth.models import User
from rest_framework import serializers, validators

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
