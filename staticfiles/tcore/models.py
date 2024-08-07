from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class Contact(models.Model):

     fullname=models.CharField(max_length=30,verbose_name=_('Ad Soyad'))
     phone=models.CharField(max_length=11,verbose_name=_('Telefon'))   
     email=models.EmailField(verbose_name=_('E-posta'))
     message=models.TextField(verbose_name=_('Mesaj'))


class About(models.Model):
     title=models.CharField(max_length=30,verbose_name=_('Başlık'))
     content=RichTextField(verbose_name=_('İçerik'))

class Service(models.Model):
     title=models.CharField(max_length=30,verbose_name=_('Başlık'))
     content=RichTextField(verbose_name=_('İçerik'))
     slug=models.SlugField(max_length=30,blank=True,editable=False)


     def save(self,*args,**kwargs):
          if not self.slug:
               self.slug=slugify(self.title)
          super(Service,self).save(*args,**kwargs)



class Slider(models.Model):
     title=models.CharField(max_length=30,verbose_name=_('Başlık'))
     image=models.ImageField(upload_to='slider',verbose_name=_('Görsel'))



class Category(models.Model):
     name=models.CharField(max_length=30,verbose_name=_('Kategori Adı'))
     slug=models.SlugField(max_length=30,editable=False)

     def save(self,*args,**kwargs):
          if not self.slug:
               self.slug=slugify(self.name)
          super(Category,self).save(*args,**kwargs)

     def  __str__(self) -> str:
          return self.name



class Blog(models.Model):
     title=models.CharField(max_length=30,verbose_name=_('Başlık'))
     image=models.ImageField(upload_to='blog',verbose_name=_('Görsel'))
     content=RichTextField(verbose_name=_('İçerik'))
     category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=_('Kategori'))
     created_at=models.DateField(auto_now_add=True,verbose_name=_('Oluşuturulma Zamanı'))
     updated_at=models.DateField(auto_now=True,verbose_name=_('Güncellenme Zamanı'))
     views=models.IntegerField(default=0,verbose_name=_('Görüntüleme'))
     slug=models.SlugField(max_length=30,unique=True,blank=True,editable=False)
     tags=TaggableManager()
     def save(self,*args,**kwargs):
          if not self.slug:
               self.slug=slugify(self.title)
          super(Blog,self).save(*args,**kwargs)


class Setting(models.Model):
     logo1=models.ImageField(upload_to='dimg',null=True,blank=True,verbose_name=_('Logo 1'))
     logo2=models.ImageField(upload_to='dimg',null=True,blank=True,verbose_name=_('Logo 2'))
     title=models.CharField(max_length=100,verbose_name=_('Başlık'))
     description=models.CharField(max_length=255,verbose_name=_('Açıklama'))
     keywords=models.CharField(max_length=255,verbose_name=_('Anaktar Kelimeler'))
     phohe_fixed=models.CharField(max_length=10,verbose_name=_('Sabit Telefon'))
     phohe_mobil=models.CharField(max_length=10,verbose_name=_('Cep Telefonu'))
     fax=models.CharField(max_length=10,verbose_name=_('Faks'))
     email=models.CharField(max_length=100,verbose_name=_('E-posta'))
     city=models.CharField(max_length=100,verbose_name=_('Şehir'))
     district=models.CharField(max_length=100,verbose_name=_('İlçe'))
     Address=models.TextField(verbose_name=_('Adres'))
     postal_code=models.CharField(max_length=7,verbose_name=_('Posta Kodu'))
     facebook_url=models.URLField(max_length=255,verbose_name=_('Facebook Adresi'))
     instagram_url=models.URLField(max_length=255,verbose_name=_('Instagram Adresi'))
     youtube_url=models.URLField(max_length=255,verbose_name=_('Youtube Adresi'))
     x_url=models.URLField(max_length=255,verbose_name=_('X Adresi'))


class Page(models.Model):
     title=models.CharField(max_length=100,verbose_name=_('Başlık'))
     content=RichTextField(verbose_name=_('İçerik'))
     slug=models.SlugField(max_length=200,blank=True,editable=False)
     def get_absolute_url(self):
          return reverse('page-detail',kwargs={'slug':self.slug})
     
     def save(self,*args,**kwargs):
          if not self.slug:
               self.slug=slugify(self.title)
          super(Page,self).save(*args,**kwargs)