from django.shortcuts import render
from .models import Credencial, LogAcesso
from django.contrib.auth.decorators import login_required

@login_required
def lista_senhas(request):
    # RF02: Lista de credenciais do utilizador
    credenciais = Credencial.objects.filter(dono=request.user)
    
    # RF05: Histórico de acessos recentes
    logs = LogAcesso.objects.filter(usuario=request.user).order_by('-data_hora')[:5]
    
    # RF06: Contador para o Alerta de Senhas Fracas (menos de 8 caracteres)
    alertas_count = sum(1 for c in credenciais if len(c.senha_exibida) < 8)
    
    context = {
        'credenciais': credenciais,
        'logs': logs,
        'alertas_count': alertas_count,
        'total_senhas': credenciais.count(),
    }
    return render(request, 'dashboard.html', context)