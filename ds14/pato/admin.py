from django.contrib import admin
from .models import DonoPato, Pato
from django.contrib.auth.admin import UserAdmin

class DonoDoPatoAdmin(UserAdmin):
    list_display= ['username','is_active','foto_de_perfil']
    fieldsets = UserAdmin.fieldsets + (
        ('Campos novos',{'fields':('nome','foto_de_perfil')}),

    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos novos',{'fields':('nome','foto_de_perfil')}),

    )

admin.site.register(Pato)
admin.site.register(DonoPato,DonoDoPatoAdmin)
