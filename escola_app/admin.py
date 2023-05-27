from django.contrib import admin

from escola_app.models import Aluno, Curso, Disciplina, Turma


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'created_at', 'updated_at')
    list_display_links = ('nome',)
    empty_value_display = '--'
    search_fields = ('nome',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'horas_aulas', 'obrigatoria', 'all_cursos')
    list_display_links = ('nome',)
    empty_value_display = '--'
    search_fields = ('nome',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'all_disciplinas')
    list_display_links = ('nome',)
    empty_value_display = '--'
    search_fields = ('nome',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'curso', 'created_at', 'updated_at')
    list_display_links = ('nome',)
    empty_value_display = '--'
    search_fields = ('nome', 'ano', 'curso')
    readonly_fields = ('created_at', 'updated_at')
