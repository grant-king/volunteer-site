from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('templates/', views.all_templates, name='all-templates'),
    path('template/new/', views.new_template, name='new-template'),
    path('template/<int:template_id>/', views.template_detail, name='template-detail'),
    path('submission/<int:submission_id>/', views.submission_detail, name='submission-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
