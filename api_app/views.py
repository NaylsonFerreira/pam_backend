from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api_app.serializers import (AlunoSerializer, CursoSerializer,
                                 DisciplinaSerializer, TurmaSerializer)
from escola_app.models import Aluno, Curso, Disciplina, Turma


class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['__all__']
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'nome', 'idade']


class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['__all__']
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'descricao']


class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['__all__']
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'descricao', 'obrigatoria', 'horas_aulas']


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['__all__']
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'nome', 'ano', 'turno', 'curso']
