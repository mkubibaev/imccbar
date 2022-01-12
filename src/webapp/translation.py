from modeltranslation.translator import register, TranslationOptions
from webapp.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
    required_languages = ('zh-cn', 'ru', 'en')

