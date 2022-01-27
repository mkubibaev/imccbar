from django.views.generic import TemplateView, ListView, DetailView

from core.settings import PAGINATION_COUNT
from webapp.models import News, AboutCenterPage, OrgStructurePage, PhotoAlbum, PhotoAlbumImage, \
    CooperationPage, ServicesPage


class HomeView(TemplateView):
    template_name = 'webapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')[:6]
        photo_album = PhotoAlbum.objects.last()
        if photo_album:
            context['photo_album'] = photo_album
            context['photos'] = PhotoAlbumImage.objects.filter(album=photo_album)[:3]
        return context


class AboutCenterView(TemplateView):
    template_name = 'webapp/about-center.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutCenterPage.objects.first()
        return context


class OrgStructurePageView(TemplateView):
    template_name = 'webapp/org-structure.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org'] = OrgStructurePage.objects.first()
        return context


class PhotoGalleryListView(ListView):
    model = PhotoAlbum
    context_object_name = 'album_list'
    template_name = 'webapp/photo-album-list.html'
    ordering = ['-created_at']
    paginate_by = PAGINATION_COUNT


class PhotoGalleryDetailView(DetailView):
    model = PhotoAlbum
    context_object_name = 'album'
    template_name = 'webapp/photo-album-detail.html'


class CooperationPageView(TemplateView):
    template_name = 'webapp/cooperation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cooperation'] = CooperationPage.objects.first()
        return context


class ServicesPageView(TemplateView):
    template_name = 'webapp/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServicesPage.objects.first()
        return context
