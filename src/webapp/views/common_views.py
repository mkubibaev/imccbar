from itertools import chain
from operator import attrgetter

from django.utils.http import urlencode

from django.views.generic import TemplateView, ListView, DetailView

from core.settings import PAGINATION_COUNT
from webapp.models import News, AboutCenterPage, OrgStructurePage, PhotoAlbum, PhotoAlbumImage, \
    CooperationPage, ServicesPage, FAQPage, ContactsPage, LinksPage, AboutCenterPreview, \
    OrgStructurePreview, VideoItem


class HomeView(TemplateView):
    template_name = 'webapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')[:6]
        context['org_structure_preview'] = OrgStructurePreview.objects.first()
        context['about_center_preview'] = AboutCenterPreview.objects.first()
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


class MultimediaView(ListView):
    context_object_name = 'media_list'
    ordering = ['-created_at']
    template_name = 'webapp/multimedia-list.html'
    paginate_by = PAGINATION_COUNT

    def get_queryset(self):
        photo_albums = PhotoAlbum.objects.all()
        videos = VideoItem.objects.all()
        result_list = chain(photo_albums, videos)
        return sorted(result_list, key=attrgetter('created_at'), reverse=True)


class PhotoGalleryDetailView(DetailView):
    model = PhotoAlbum
    context_object_name = 'album'
    template_name = 'webapp/photo-album-detail.html'


class VideDetailView(DetailView):
    model = VideoItem
    context_object_name = 'video_item'
    template_name = 'webapp/video-detail.html'


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


class FAQPageView(TemplateView):
    template_name = 'webapp/FAQ.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faq'] = FAQPage.objects.first()
        return context


class ContactsPageView(TemplateView):
    template_name = 'webapp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactsPage.objects.first()
        return context


class LinksPageView(TemplateView):
    template_name = 'webapp/links.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = LinksPage.objects.first()
        return context


class SearchResultsView(ListView):
    template_name = 'webapp/search-results.html'
    context_object_name = 'search_results'
    paginate_by = PAGINATION_COUNT

    def __init__(self):
        super().__init__()
        self.query = None

    def get_queryset(self):
        self.query = self.request.GET.get('q')
        if self.query and len(self.query) >= 2:
            news = News.objects.filter(title__icontains=self.query).order_by('-created_at')
            photoalbums = PhotoAlbum.objects.filter(title__icontains=self.query).order_by('-created_at')
            videos = VideoItem.objects.filter(title__icontains=self.query).order_by('-created_at')
            for n in news:
                n.model_type = 'news'
            for photoalbum in photoalbums:
                photoalbum.model_type = 'photo'
            for video in videos:
                video.model_type = 'video'
            return list(chain(news, photoalbums, videos))
        return News.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.query:
            context['query'] = urlencode({'q': self.query})
        return context
