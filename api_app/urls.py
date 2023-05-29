from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api_app.views import (AlunoViewSet, CursoViewSet, DisciplinaViewSet,
                           TurmaViewSet)

router = DefaultRouter()
router.register(r'aluno', AlunoViewSet)
router.register(r'curso', CursoViewSet)
router.register(r'disciplina', DisciplinaViewSet)
router.register(r'turma', TurmaViewSet)

app_name = 'api_app'
urlpatterns = [
    path('login/', obtain_auth_token, name='api_login'),
    path('', include(router.urls)),
]
