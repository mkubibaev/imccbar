from django.views.generic import ListView, DetailView
from core.settings import PAGINATION_COUNT
from webapp.models import News


class NewsListView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'webapp/news/news-list.html'
    ordering = ['-created_at']
    paginate_by = PAGINATION_COUNT


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'webapp/news/news-detail.html'

