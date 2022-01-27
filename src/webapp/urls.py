from django.urls import path

from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-center', views.AboutCenterView.as_view(), name='about_center'),
    path('organization-structure', views.OrgStructurePageView.as_view(), name='org_structure'),
    path('news', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('multimadia', views.PhotoGalleryListView.as_view(), name='album_list'),
    path('multimadia/<int:pk>', views.PhotoGalleryDetailView.as_view(), name='album_detail'),
    path('cooperation-and-exchange', views.CooperationPageView.as_view(), name='cooperation_page'),
    path('platform-services', views.ServicesPageView.as_view(), name='platform_services'),
]
