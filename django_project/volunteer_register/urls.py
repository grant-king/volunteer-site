from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('templates/', views.all_templates, name='all-templates'),
    path('template/<int:template_id>/', views.template_detail, name='template-detail'),
    path('submission/<int:submission_id>/', views.submission_detail, name='submission-detail'),
]