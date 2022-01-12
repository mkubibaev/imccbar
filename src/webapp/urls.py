from django.urls import path

from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]