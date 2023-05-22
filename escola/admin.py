from django.contrib import admin
from escola.models import Aluno, Curso

class ListaAlunos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cpf', 'matricula', 'email', 'data_nascimento', 'cidade']
    list_display_links = ["id", "nome"]
    list_editable = ["email"]
    search_fields = ["nome"]
    list_filter = ["cidade", "nome"]
    list_per_page = 10

admin.site.register(Aluno, ListaAlunos)

class ListaCursos(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'nome', 'vagas']
    list_display_links = ["id"]
    list_editable = ["nome", "vagas"]
    search_fields = ["nome"]
    list_filter = ["nome"]
    list_per_page = 10

admin.site.register(Curso, ListaCursos)