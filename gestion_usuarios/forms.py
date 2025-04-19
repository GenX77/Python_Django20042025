from django import forms
from .models import Contacto

# Lista de palabras prohibidas
palabras_prohibidas = [
    'culo', 'pene', 'vagina', 'gilipollas', 'cabrón', 'zorra', 'mierda', 'joder',
    'coño', 'teta', 'polla', 'maricón', 'puta', 'chingar', 'mamón', 'idiota',
    'imbécil', 'estúpido', 'carajo', 'pendejo', 'boludo', 'concha', 'verga',
    'pendeja', 'zorras', 'cabrones', 'gilipollas', 'maricones', 'putas',
    'mamon', 'idiotas', 'imbeciles', 'estupidos', 'carajos', 'pendejos',
    'boludos', 'conchas', 'vergas', 'pendejas',
    'marica', 'subnormal', 'lesbiana', 'lesbianas', 'lesbi',
    'marikas', 'maricones'
    # Puedes añadir más palabras y variaciones a esta lista
]

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'email']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            for palabra in palabras_prohibidas:
                if palabra in nombre.lower():
                    raise forms.ValidationError(f"El nombre contiene la palabra no permitida: '{palabra}'.")
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            for palabra in palabras_prohibidas:
                if palabra in telefono.lower():
                    raise forms.ValidationError(f"El teléfono contiene la palabra no permitida: '{palabra}'.")
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            for palabra in palabras_prohibidas:
                if palabra in email.lower():
                    raise forms.ValidationError(f"El email contiene la palabra no permitida: '{palabra}'.")
        return email