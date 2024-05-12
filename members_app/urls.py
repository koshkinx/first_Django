from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_page, name='input_page'),
    path('save/', views.save_input, name='save_input'),
    path('display/', views.display_page, name='display_input'),
    path('session/', views.session_page, name='session_page'),
]
