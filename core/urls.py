from django.urls import path
from core.views import index, contato, produto


urlpatterns = [
    path('contato', contato),
    path('', index, name='index'),
    path('produto/<int:pk>', produto, name='produto'),

]