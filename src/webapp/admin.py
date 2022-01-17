from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from webapp.models import News, AboutCenterPage


class BaseAdmin(TranslationAdmin):
    exclude = []
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(News, BaseAdmin)
admin.site.register(AboutCenterPage, BaseAdmin)