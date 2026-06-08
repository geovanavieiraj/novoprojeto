from django import forms
from .models import Credencial

class CredencialForm(forms.ModelForm):
    class Meta:
        model = Credencial
        fields = ['site_nome', 'login_usuario', 'senha_exibida', 'categoria']
        widgets = {
            'senha_exibida': forms.PasswordInput(render_value=True, attrs={'id': 'campo-senha'}),
        }