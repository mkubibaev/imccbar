from modeltranslation.translator import register, TranslationOptions
from webapp.models import News, AboutCenterPage, OrgStructurePage, PhotoAlbum, \
    CooperationPage, ServicesPage


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
    required_languages = ('zh-cn', 'ru', 'en')


@register(AboutCenterPage)
class AboutCenterPageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(OrgStructurePage)
class OrgStructurePageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(PhotoAlbum)
class PhotoAlbumTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(CooperationPage)
class CooperationPageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(ServicesPage)
class ServicesPageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')

