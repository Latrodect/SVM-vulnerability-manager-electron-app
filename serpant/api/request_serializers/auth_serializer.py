from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    """
    Sign in serializer accepts username and password. 
    
    Variables:
    username(required)
    password(required)
    """
    username = serializers.CharField(help_text='Username')
    password = serializers.CharField(help_text='Password')