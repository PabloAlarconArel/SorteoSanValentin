from rest_framework import serializers
from django.contrib.auth import authenticate
import re

class SetPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        password= data['password']

        if len(password) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'\d', password):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[A-Z]', password):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'[a-z]', password):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra minúscula.")
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        
        return data
    
    def save(self,user):
        password = self.validated_data['password']
        user.set_password(password)
        user.is_active =True
        user.is_verified = True
        user.save()
        return user


class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("La cuenta está desactivada.")
                if not user.is_staff:
                    raise serializers.ValidationError("No tienes permisos de administrador.")
            else:
                raise serializers.ValidationError("Credenciales incorrectas.")
        else:
            raise serializers.ValidationError("Se deben proporcionar ambos campos: email y contraseña.")
        
        data['user'] = user
        return data

