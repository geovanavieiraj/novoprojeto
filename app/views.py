from django.shortcuts import render, redirect
from .models import Credencial, Categoria, LogAcesso # Importando o que está no seu documento

def dashboard(request):
    # RF06: Lógica para Alerta de Senhas Fracas
    credenciais = Credencial.objects.filter(dono=request.user)
    alertas = [c for c in credenciais if len(c.senha_exibida) < 8]
    
    context = {
        'credenciais': credenciais,
        'alertas_count': len(alertas), # RF06
    }
    return render(request, 'dashboard.html', context)
def lista_senhas(request):
    return render(request, 'lista_senhas.html')
from django.shortcuts import render

def lista_senhas(request):
    dados = [
        {'site': 'Instagram', 'usuario': '@jose', 'dica': 'Nome do cão + 2024'},
        {'site': 'Netflix', 'usuario': 'jose@email.com', 'dica': 'Série favorita'},
    ]
    return render(request, 'lista_senhas.html', {'senhas': dados})

def adicionar_senha(request):
    return render(request, 'adicionar_senha.html')