from django.contrib import admin

from .models import Produto, Cliente

class Produto_info(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')




admin.site.register(Produto, Produto_info)
admin.site.register(Cliente)
