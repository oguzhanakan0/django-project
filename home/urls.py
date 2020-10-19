from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/load-tenures/', views.load_tenures, name='ajax_load_tenures'),  # <-- this one here
    path('ajax/get-principal-limits/', views.get_principal_limits, name='ajax_get_principal_limits'),  # <-- this one here
]