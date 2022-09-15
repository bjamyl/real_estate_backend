from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields =['first_name', 'last_name','username','email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords do not match!'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error': 'Username is already taken'})
        
        account = User(email=email,username=username,first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.save()
        
        return account
    
        