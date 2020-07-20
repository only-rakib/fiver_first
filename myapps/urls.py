from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('our_vision/', views.ourVisionView, name='our_vision'),
    path('careers_mentor/', views.careersMentorView, name='careers_mentor'),
    path('mentor_team/', views.mentorTeamView, name='mentor_team'),
    path('contact/', views.contactView, name='contact'),
    path('donate/', views.donateView, name='donate'),
    path('become_a_sponsor/', views.BecomeaSponsorView, name='become_a_sponsor'),
    path('under_construction/', views.UnderConstructionView,
         name='under_construction'),
    path('annual_report2016/', views.annualReportView,
         name='annual_report2016'),
]
