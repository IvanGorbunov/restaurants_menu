from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('menu/', views.MenuViewSet.as_view({'get': 'list', }), name='list'),
]
