from django.views.generic import TemplateView
from webapp.models import News


class HomeView(TemplateView):
    template_name = 'webapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')[:6]
        return context
