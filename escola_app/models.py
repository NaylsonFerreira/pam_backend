from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe

TURNOS = [
    ('manha', 'Manhã'),
    ('tarde', 'Tarde'),
    ('noite', 'Noite'),
]


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.nome}'


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(
        'Descrição', max_length=100,
        null=True, blank=True
    )
    obrigatoria = models.BooleanField('Obrigatória', default=True)
    horas_aulas = models.PositiveIntegerField(default=40)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def all_cursos(self):
        cursos = Curso.objects.filter(disciplinas__id=self.id)
        html = ''
        for c in cursos:
            html += f'<p><a href="/escola_app/curso/{c.id}">{c.nome}</a></p>'
        return mark_safe(html)
    all_cursos.short_description = 'Cursos'

    def __str__(self):
        return f'{self.nome}'


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(
        'Descrição', max_length=100,
        null=True, blank=True
    )
    disciplinas = models.ManyToManyField(Disciplina)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def all_disciplinas(self):
        disciplina_list = self.disciplinas.all()
        html = ''
        for d in disciplina_list:
            html += f'<p><a href="/escola_app/disciplina/{d.id}">{d.nome}</a></p>'
        return mark_safe(html)
    all_disciplinas.short_description = 'Disciplinas'

    def __str__(self):
        return f'{self.nome}'


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.PositiveIntegerField(default=2023)
    turno = models.CharField(choices=TURNOS, default=TURNOS[0], max_length=10)
    alunos = models.ManyToManyField(Aluno)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.nome}-{self.ano}'
