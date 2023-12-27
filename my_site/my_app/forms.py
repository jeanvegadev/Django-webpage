from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

        error_messages = {
            "age":{
                'max_value': "Tú edad no debe ser más de 100"
            }
        }


class LoginForm(AuthenticationForm):
    # You can customize the form if needed
    pass