from django.urls import path

from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-center', views.AboutCenterView.as_view(), name='about_center'),
    path('organization-structure', views.OrgStructurePageView.as_view(), name='org_structure'),
    path('news', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('multimadia', views.MultimediaView.as_view(), name='media_list'),
    path('multimadia/photogallery/<int:pk>', views.PhotoGalleryDetailView.as_view(), name='album_detail'),
    path('multimadia/video/<int:pk>', views.VideDetailView.as_view(), name='video_detail'),
    path('cooperation-and-exchange', views.CooperationPageView.as_view(), name='cooperation_page'),
    path('platform-services', views.ServicesPageView.as_view(), name='platform_services'),
    path('faq', views.FAQPageView.as_view(), name='faq'),
    path('contacts', views.ContactsPageView.as_view(), name='contacts'),
    path('links', views.LinksPageView.as_view(), name='links'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
