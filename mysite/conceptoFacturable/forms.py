from django import forms
from .models import ConceptoFacturable


class ConceptoFacturableForm(forms.ModelForm):

    class Meta:
        model = ConceptoFacturable
        fields = {
                    'concepto',
                    'clase_concepto',
                    'operador',
                    'tipo_comunicacion',
                    'concepto_operador',
                    'ambito'
                 }
