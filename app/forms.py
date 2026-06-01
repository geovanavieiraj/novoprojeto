from django import forms
from .models import Credencial

class CredencialForm(forms.ModelForm):
    class Meta:
        model = Credencial
        fields = ['site_nome', 'url_site', 'usuario_site', 'senha_armazenada', 'categoria', 'e_favorito', 'notas']
        widgets = {
            'senha_armazenada': forms.PasswordInput(render_value=True, attrs={'id': 'campo-senha'}),
        }