from django.urls import path
from . import views

urlpatterns = [
    path("",views.project_index, name="proyectos"),
    path("<int:pk>/",views.project_description,name="detalle_proyecto"),
]