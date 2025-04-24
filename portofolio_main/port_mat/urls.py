from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path
from .views import HomeView, AboutView, ProjectsView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]
