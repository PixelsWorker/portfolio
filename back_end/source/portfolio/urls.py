from django.urls import path
from .views import HomeView, AboutView, ProjectsView, ContactView, ProjectDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]


