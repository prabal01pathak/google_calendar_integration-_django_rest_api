from django.urls import path

from . import views

urlpatterns = [
    path('v1/calendar/init/', views.GoogleCalendarInitView, name='google_calendar_init'),
    path('v1/calendar/redirect/', views.GoogleCalendarRedirectView, name='google_calendar_redirect'),
]