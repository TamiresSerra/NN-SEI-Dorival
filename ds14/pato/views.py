from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Pato
from .serializers import PatoSerializer, LoginSerializer, DonoDoPatoSerializer, LoginSerializer2
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

class PatoPaginacao(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

class PatoListCreateAPIView(ListCreateAPIView):
    queryset = Pato.objects.all()
    serializer_class = PatoSerializer
    pagination_class = PatoPaginacao
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

    def perform_create(self, serializer):
        if serializer.validated_data['peso'] < 0:
            raise serializers.ValidationError("O peso não pode ser negativo")
        serializer.save()

class PatoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pato.objects.all()
    serializer_class = PatoSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        idade = request.data.get('idade')

        if idade is not None and int(idade) < 0:
            return Response({'erro': 'A idade não pode ser negativa.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)

class loginView(CreateAPIView):
    serializer_class = LoginSerializer 
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_execption=True)

        usuario = serializer.validated_data['usuario']
        usuario_serializer = DonoDoPatoSerializer(usuario)

        return Response({
            'usuario': usuario_serializer.data,
            'refresh': serializer.validated_data['refresh'],
            'access': serializer.validated_data['access']
        }, status=HTTP_200_OK)
    
class LoginView2(TokenObtainPairView):
    serializer_class = LoginSerializer2