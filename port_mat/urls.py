from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path
from .views import HomeView, AboutView, ProjectsView, ContactView, ServicesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServicesView.as_view(), name='services'),]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
