from modeltranslation.translator import register,TranslationOptions
from .models import About, Blog, Category, Page,Service,Setting,Announcement

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields=('title','content')

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields=('title','content')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields=('name',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields=('title','content')

@register(Setting)
class SettingTranslationOptions(TranslationOptions):
    fields=('title','description','keywords')

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields=('title','content')

@register(Announcement)
class PageTranslationOptions(TranslationOptions):
    fields=('title','content')