from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView  # <-- Importar esta función
from mascotas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirigir la ruta raíz a /mascotas
    path('', RedirectView.as_view(url='/mascotas', permanent=False)),
    
    # Rutas Responsable
    path('responsable/crear', views.crear_responsable),
    path('responsables', views.listar_responsable),
    path('responsable/modificar/<int:pk>', views.modificar_responsable),
    path('responsable/eliminar/<int:pk>', views.eliminar_responsable),
    
    # Rutas Mascota
    path('mascota/crear', views.crear_mascota),
    path('mascotas', views.listar_mascotas),
    path('mascota/modificar/<int:pk>', views.modificar_mascota),
    path('mascota/eliminar/<int:pk>', views.eliminar_mascota),
]