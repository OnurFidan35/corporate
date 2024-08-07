from django.contrib import admin
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from .admin_mixins import CommonMedia
from .models import About, Blog, Category, Contact, Page, Service, Setting, Slider
from  modeltranslation.admin import TranslationAdmin

from  tcore import models


class BaseAdmin(admin.ModelAdmin):
     def has_add_permission(self, request,obj=None):
          return False

     def has_delete_permission(self, request, obj=None) -> bool:
          return False



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=[

        ('fullname'),
        ('phone'),
        ('email'),

    ]

@admin.register(About)
class AboutAdmin(TranslationAdmin,CommonMedia,BaseAdmin):
    list_display=('title',)

    group_fieldsets=True



    


@admin.register(Service)
class ServiceAdmin(TranslationAdmin,CommonMedia):
     list_display=('title',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
     list_display=('title','image')

@admin.register(Category)
class CategoryAdmin(TranslationAdmin,CommonMedia):
     list_display=('name',)
    
@admin.register(Blog)
class BlogAdmin(TranslationAdmin,CommonMedia):
     list_display=('title','views','image','created_at','updated_at')

@admin.register(Setting)
class SettingAdmin(TranslationAdmin,CommonMedia,BaseAdmin):
     list_display=('title',)

@admin.register(Page)
class PageAdmin(TranslationAdmin,CommonMedia):
     list_display=('title','slug_url')

     def slug_url(self,obj):
          url=obj.get_absolute_url()
          return url
     
     slug_url.short_description='Detay Linki'