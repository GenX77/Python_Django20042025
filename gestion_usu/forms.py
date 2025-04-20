# RENDER-DEPLY-TUTORIAL-DJANGO-CODE/gestion_usu/forms.py
from django import forms

palabras_prohibidas = [
    'culo', 'pene', 'vagina', 'gilipollas', 'cabrón', 'zorra', 'mierda', 'joder',
    'coño', 'teta', 'polla', 'maricón', 'puta', 'chingar', 'mamón', 'idiota',
    'imbécil', 'estúpido', 'carajo', 'pendejo', 'boludo', 'concha', 'verga',
    'pendeja', 'zorras', 'cabrones', 'gilipollas', 'maricones', 'putas',
    'mamon', 'idiotas', 'imbeciles', 'estupidos', 'carajos', 'pendejos',
    'boludos', 'conchas', 'vergas', 'pendejas'
    # Puedes añadir más palabras a esta lista
]

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    telefono = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=100, required=True)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].lower()
        for palabra in palabras_prohibidas:
            if palabra in nombre:
                raise forms.ValidationError(f"La palabra '{palabra}' no está permitida en el nombre.")
        return self.cleaned_data['nombre']

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono'].lower()
        for palabra in palabras_prohibidas:
            if palabra in telefono:
                raise forms.ValidationError(f"La palabra '{palabra}' no está permitida en el teléfono.")
        return self.cleaned_data['telefono']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        for palabra in palabras_prohibidas:
            if palabra in email:
                raise forms.ValidationError(f"La palabra '{palabra}' no está permitida en el email.")
        return self.cleaned_data['email']