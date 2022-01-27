from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from webapp.models import News, AboutCenterPage, OrgStructurePage, PhotoAlbum, PhotoAlbumImage, \
    CooperationPage, ServicesPage


class BaseAdmin(TranslationAdmin):
    exclude = []
    readonly_fields = ('created_at', 'updated_at')


class PhotoAlbumImageAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ('get_image', 'album')
    list_filter = ('album',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 50

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.thumbnail.url} width="auto" height="50">')

    get_image.short_description = 'Photo'


admin.site.register(News, BaseAdmin)
admin.site.register(AboutCenterPage, BaseAdmin)
admin.site.register(OrgStructurePage, BaseAdmin)
admin.site.register(CooperationPage, BaseAdmin)
admin.site.register(ServicesPage, BaseAdmin)
admin.site.register(PhotoAlbum, BaseAdmin)
admin.site.register(PhotoAlbumImage, PhotoAlbumImageAdmin)
