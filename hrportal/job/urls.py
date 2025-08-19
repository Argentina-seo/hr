from django.urls import path, re_path, register_converter
from . import views

urlpatterns = [
    path('', views.index, name='home'), #главная страница по курьерам
    path('job/<int:job_id>/', views.show_job, name='vacancy'),   # пеший
    path('apply/', views.apply, name='apply'),
]
