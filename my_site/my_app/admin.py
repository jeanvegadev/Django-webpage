from django.contrib import admin
from my_app.models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('NOMBRES',{'fields':['first_name', 'last_name']}),
        ('EDAD',{'fields':['age']})
    ]