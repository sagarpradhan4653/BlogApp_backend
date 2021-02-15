from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from . models import Blogger


class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogger
        fields = ('id','title','user','category','picture','date','description')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only':True, 'required':True}} # this is for not displaying password and enable to create new user

    
    def create(self,validate_data): # create new user
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user) # create token while adding new user to db
        return user




