from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from webapp.models import News, AboutCenterPage, OrgStructurePage, PhotoAlbum, PhotoAlbumImage, \
    CooperationPage, ServicesPage, FAQPage, ContactsPage, LinksPage, AboutCenterPreview,\
    OrgStructurePreview, VideoItem


class BaseAdmin(TranslationAdmin):
    exclude = []
    readonly_fields = ('created_at', 'updated_at')


class BaseAdminDate(BaseAdmin):
    list_display = ('title', 'created_at',)


class SinglePageAdmin(BaseAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PhotoAlbumImageAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ('get_image', 'album')
    list_filter = ('album',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 50

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.thumbnail.url} width="auto" height="50">')

    get_image.short_description = 'Photo'


admin.site.register(News, BaseAdminDate)
admin.site.register(AboutCenterPage, SinglePageAdmin)
admin.site.register(OrgStructurePage, SinglePageAdmin)
admin.site.register(CooperationPage, SinglePageAdmin)
admin.site.register(ServicesPage, SinglePageAdmin)
admin.site.register(FAQPage, SinglePageAdmin)
admin.site.register(ContactsPage, SinglePageAdmin)
admin.site.register(LinksPage, SinglePageAdmin)
admin.site.register(PhotoAlbum, BaseAdminDate)
admin.site.register(VideoItem, BaseAdminDate)
admin.site.register(PhotoAlbumImage, PhotoAlbumImageAdmin)
admin.site.register(AboutCenterPreview, SinglePageAdmin)
admin.site.register(OrgStructurePreview, SinglePageAdmin)
