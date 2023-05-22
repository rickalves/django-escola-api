from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializers import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Retorna todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Retorna todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer





