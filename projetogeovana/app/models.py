from django.db import models
from django.contrib.auth.models import User

# 01. Perfil (RF01)
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lembrete_mestre = models.CharField(max_length=255, blank=True)
    class Meta: verbose_name_plural = "Perfis de Usuários"

# 02. Categorias (RF03)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    class Meta: verbose_name_plural = "Categorias"
    def __str__(self): return self.nome

# 03. Credenciais (RF02)
class Credencial(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    site_nome = models.CharField(max_length=100)
    login_usuario = models.CharField(max_length=100)
    senha_exibida = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: verbose_name_plural = "Credenciais"

# 04. Logs (RF05)
class LogAcesso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    credencial_nome = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name_plural = "Logs de Acessos"

# 05. Histórico (RF07)
class HistoricoSenha(models.Model):
    credencial = models.ForeignKey(Credencial, on_delete=models.CASCADE)
    senha_antiga = models.CharField(max_length=255)
    data_alteracao = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name_plural = "Histórico de Senhas"

# 06. Alertas (RF06)
class AlertaSeguranca(models.Model):
    credencial = models.ForeignKey(Credencial, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100)
    class Meta: verbose_name_plural = "Alertas de Segurança"

# 07. Gerador (RF04)
class GeradorConfig(models.Model):
    tamanho = models.IntegerField(default=12)
    class Meta: verbose_name_plural = "Configuração do Gerador"

# 08. Backups
class BackupSistema(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name_plural = "Backups"

# 09. Termos de Uso (ERRO CORRIGIDO AQUI)
class TermoPrivacidade(models.Model):
    texto = models.TextField()
    class Meta: verbose_name_plural = "Termos de Uso"

# 10. Notificações
class Notificacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mensagem = models.CharField(max_length=255)
    class Meta: verbose_name_plural = "Notificações"

# 11. Suporte
class ChamadoSuporte(models.Model):
    assunto = models.CharField(max_length=200)
    aberto = models.BooleanField(default=True)
    class Meta: verbose_name_plural = "Chamados de Suporte"