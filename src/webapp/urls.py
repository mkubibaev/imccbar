from django.urls import path

from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-center', views.AboutCenterView.as_view(), name='about_center'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
]
