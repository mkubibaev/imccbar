from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from webapp.models import News


class BaseAdmin(TranslationAdmin):
    exclude = []
    save_as = True
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(News, BaseAdmin)
