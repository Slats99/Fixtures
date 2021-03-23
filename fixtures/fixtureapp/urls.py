from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', TemplateView.as_view(template_name='fixtureapp/about.html'), name='about'),
    path('team/<slug:team_id_slug>/', views.TeamView.as_view(), name='team_by_id'),
    path('wag/', views.WAGView.as_view(), name='teamWAG')
]