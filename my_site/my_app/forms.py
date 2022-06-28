from django import forms
from .models import Usuario

# class UsuarioForm(forms.Form):
#     first_name = forms.CharField(label="First name",max_length=30)
#     last_name = forms.CharField(label="Last name", max_length=30)
#     age = forms.IntegerField(label="Age")
#     email = forms.EmailField(label="Email")
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

        error_messages = {
            "age":{
                'max_value': "Tú edad no debe ser más de 100"
            }
        }