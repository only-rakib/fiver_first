from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('our_vision/', views.ourVisionView, name='our_vision'),
    path('mentor_team/', views.mentorTeamView, name='mentor_team'),
    path('careers_mentor/', views.careersMentorView, name='careers_mentor'),
    path('latest_news/', views.latestNewsView,
         name='latest_news'),
    path('contact/', views.contactView, name='contact'),
    path('donate/', views.donateView, name='donate'),
    path('become_a_sponsor/', views.BecomeaSponsorView, name='become_a_sponsor'),
    path('under_construction/', views.UnderConstructionView,
         name='under_construction'),
    path('annual_report2016/', views.annualReportView,
         name='annual_report2016'),

    path('success_stories/', views.successStoriesView,
         name='success_stories'),
    path('campaign-1/', views.campaign1View,
         name='campaign-1'),
    path('campaign-2/', views.campaign2View,
         name='campaign-2'),
    path('campaign-3/', views.campaign3View,
         name='campaign-3'),
    path('campaign-4/', views.campaign4View,
         name='campaign-4'),

    path('latest_news/<slug:slug>', views.latestNewsClickView,
         name='latest_news_click'),
    path('interact/', views.interactView,
         name='interact'),


]
