from django.contrib import admin
from .models import (
    PerfilUsuario, Categoria, Credencial, LogAcesso, 
    HistoricoSenha, AlertaSeguranca, GeradorConfig, 
    BackupSistema, TermoPrivacidade, Notificacao, ChamadoSuporte
)

meus_modelos = [
    PerfilUsuario, Categoria, Credencial, LogAcesso, 
    HistoricoSenha, AlertaSeguranca, GeradorConfig, 
    BackupSistema, TermoPrivacidade, Notificacao, ChamadoSuporte
]

for modelo in meus_modelos:
    try:
        admin.site.register(modelo)
    except admin.sites.AlreadyRegistered:
        pass