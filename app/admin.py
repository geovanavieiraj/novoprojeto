from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Credencial)
admin.site.register(LogAcesso)
admin.site.register(HistoricoSenha)
admin.site.register(AlertaSeguranca)
admin.site.register(PerfilUsuario)
admin.site.register(GeradorConfig)