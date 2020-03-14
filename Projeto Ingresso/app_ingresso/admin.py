from django.contrib import admin

from .models import Pessoa
from .models import PessoaFisica
from .models import Evento 
from .models import Inscricao
from .models import Ingresso 

@admin.register(Pessoa, PessoaFisica, Evento, Inscricao, Ingresso)


class PessoaAdmin(admin.ModelAdmin):
    pass
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass
class EventoAdmin(admin.ModelAdmin):
    pass
class IngressoAdmin(admin.ModelAdmin):
    pass
class InscricaoAdmin(admin.ModelAdmin):
    pass   

# Register your models here.
