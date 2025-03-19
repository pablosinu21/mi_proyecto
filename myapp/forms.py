from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad', 'fecha_vencimiento']
        labels = {
            'fecha_vencimiento': 'Fecha de recolección',  # Cambia la etiqueta aquí
        }
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }
