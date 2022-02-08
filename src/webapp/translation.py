from modeltranslation.translator import register, TranslationOptions
from webapp.models import News, AboutCenterPage, OrgStructurePage, PhotoAlbum, \
    CooperationPage, ServicesPage, FAQPage, ContactsPage, LinksPage, AboutCenterPreview, OrgStructurePreview


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
    required_languages = ('zh-cn', 'ru', 'en')


@register(AboutCenterPage)
class AboutCenterPageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(AboutCenterPreview)
class AboutCenterPreviewTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(OrgStructurePage)
class OrgStructurePageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(OrgStructurePreview)
class OrgStructurePreviewTranslationOptions(TranslationOptions):
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


@register(FAQPage)
class FAQPageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(ContactsPage)
class ContactsPageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')


@register(LinksPage)
class LinksPageTranslationOptions(TranslationOptions):
    fields = ('body',)
    required_languages = ('zh-cn', 'ru', 'en')

