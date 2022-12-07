from django import forms

class FormularioEmpres(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    numero = forms.NumberInput()
    cpf = forms.NumberInput()