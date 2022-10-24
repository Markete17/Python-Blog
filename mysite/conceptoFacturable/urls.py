from django.urls import path
from . import views

urlpatterns = [
    path('', views.conceptos_facturables_list,
         name='conceptos_facturables_list'),
    path('<int:pk>', views.conceptos_facturables_detail,
         name='conceptos_facturables_detail'),
    path("nuevo", views.conceptos_facturables_nuevo,
         name='conceptos_facturables_nuevo'),
    path("<int:pk>/editar", views.conceptos_facturables_editar,
         name='conceptos_facturables_editar'),
]
