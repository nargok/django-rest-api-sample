from rest_framework import serializers
from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id' ,'name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
  # authorのserializerを上書きする
  author = UserSerializer(read_only=True)

  class Meta:
    model = Entry
    fields = ('id', 'title', 'body', 'created_at', 'status', 'author')