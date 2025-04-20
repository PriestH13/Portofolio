from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [ 
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('projects/', views.projects, name='projects'),
     path('contact/', views.contact, name='contact'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)