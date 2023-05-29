from rest_framework import serializers

from escola_app.models import Aluno, Curso, Disciplina, Turma


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        exclude = ('created_at', 'updated_at')


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        exclude = ('created_at', 'updated_at')


class CursoSerializer(serializers.ModelSerializer):
    disciplinas = DisciplinaSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        exclude = ('created_at', 'updated_at')


class TurmaSerializer(serializers.ModelSerializer):
    alunos = AlunoSerializer(many=True, read_only=True)
    curso = CursoSerializer(read_only=True)

    class Meta:
        model = Turma
        exclude = ('created_at', 'updated_at')
