from rest_framework import serializers
from .models import RecomendacionPersonal, RecomendacionUsuario
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializador para manejar la información relacionada con los usuarios, utilizando el modelo de User de Django.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

class RecomendacionPersonalSerializer(serializers.ModelSerializer):
    """
    Serializador para manejar datos relacionados con mis propias recomendaciones acerca de cualquier tipo de multimedia.
    """
    class Meta:
        model = RecomendacionPersonal
        fields = '__all__'

class RecomendacionUsuarioSerializer(serializers.ModelSerializer):
    """
    Serializador para manejar datos relacionados con las recomendaciones que los usuarios van a crear en mi sitio web.
    """
    class Meta:
        model = RecomendacionUsuario
        fields = '__all__'