from django.db import models
from django.contrib.auth.models import User

# Requisito Estrutural (RF03) 
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    class Meta: verbose_name_plural = "Categorias"
    def __str__(self): return self.nome

# Requisito Principal (RF02) 
class Credencial(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE) # RF01 
    site_nome = models.CharField(max_length=100, verbose_name="App ou Site")
    login_usuario = models.CharField(max_length=100)
    senha_exibida = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    class Meta: verbose_name_plural = "Credenciais"
    def __str__(self): return f"{self.site_nome} ({self.login_usuario})"

# Monitoramento e Auditoria (RF05) 
class LogAcesso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    credencial_nome = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name_plural = "Logs de Acessos"

# Segurança e Histórico (RF07) 
class HistoricoSenha(models.Model):
    credencial = models.ForeignKey(Credencial, on_delete=models.CASCADE)
    senha_antiga = models.CharField(max_length=255)
    data_alteracao = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name_plural = "Histórico de Senhas"

# Inteligência de Dados (RF06) 
class AlertaSeguranca(models.Model):
    credencial = models.ForeignKey(Credencial, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100, choices=[('FRACA', 'Senha Fraca'), ('REPETIDA', 'Senha Repetida')])
    data_criacao = models.DateTimeField(auto_now_add=True)
    class Meta: verbose_name_plural = "Alertas de Segurança"

# --- Itens para completar os 11 no Admin ---
class GeradorConfig(models.Model): # Suporte ao RF04 
    tamanho_padrao = models.IntegerField(default=12)
    usar_simbolos = models.BooleanField(default=True)
    class Meta: verbose_name_plural = "Configurações do Gerador"

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lembrete_mestre = models.CharField(max_length=255, blank=True)
    class Meta: verbose_name_plural = "Perfis de Usuários"

class BackupSistema(models.Model):
    data_backup = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Concluído")
    class Meta: verbose_name_plural = "Backups Realizados"

class ExportacaoLog(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    formato = models.CharField(max_length=10, default="PDF")
    class Meta: verbose_name_plural = "Logs de Exportação"

class TermosDeUso(models.Model):
    versao = models.CharField(max_length=10)
    texto = models.TextField()
    class Meta: verbose_name_plural = "Termos e Políticas"

class NotificacaoSistema(models.Model):
    mensagem = models.CharField(max_length=255)
    lida = models.BooleanField(default=False)
    class Meta: verbose_name_plural = "Notificações do Sistema"