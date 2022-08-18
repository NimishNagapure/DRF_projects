from .models import Singer,Song,User
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields =['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True,read_only=True )
    class Meta:
        model = Singer
        fields =['id','name','gender','sungby']


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username' , 'password')
        write_only_fields = ('password')
