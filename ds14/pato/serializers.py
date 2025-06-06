from rest_framework import serializers
from .models import Pato, DonoPato
from .views import Pato
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pato
        fields = "__all__"
        read_only_fields = ('id', 'cagaTorrada')
   
class DonoDoPatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonoPato
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            usuario = authenticate(request=self.context.get('request'),
                                   username=username, password=password)
        
            if not usuario:
                mensagem = "Credencial não identificada"
                raise serializers.ValidationError(mensagem, code='authorization')
            
            if not usuario.is_active:
                mensagem = "Conta desativada"
                raise serializers.ValidationError(mensagem, code='authorization')
        
            refresh = RefreshToken.for_user(usuario)

            attrs['usuario'] = usuario
            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

            return attrs
        else:
            mensagem = "username ou senha não inseridos"
            raise serializers.ValidationError(mensagem, code='authorization')

class LoginSerializer2(TokenObtainPairSerializer):
    def validate(self, attrs):
        dados = super().validate(attrs)
        dados['usuario'] = {
            'nome': self.user.username,
            'bio': self.user.bio
        }

        return dados