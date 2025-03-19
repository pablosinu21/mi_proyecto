from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='inicio'),  # Página de inicio
    path('productos/', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
     path('producto/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
