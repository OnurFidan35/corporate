from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.utils import translation
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlparse  
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from taggit.managers import TaggableManager
from tcore.models import About, Blog, Category, Page, Service, Slider
from taggit.models import Tag
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib import messages


def set_language(request,language):
    for lang,_ in settings.LANGUAGES:
        translation.activate(lang)
        try:
           view = resolve(urlparse(request.META.get("HTTP=REFERER")).path) 
        except Resolver404:
            view=None
        if view:
            break
        
    if view:
       translation.activate(language)
       next_url= reverse(view.url_name,args=view.args,kwargs=view.kwargs)
       response = HttpResponseRedirect(next_url)
       
    else:
       response = HttpResponseRedirect("/")
    return response


class BaseView(object):
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['Categories']=Category.objects.all()
        context['PBlogs']=Blog.objects.order_by('-views')[:5]
        context['most_common_tags'] =Tag.objects.annotate(num_times=Count('taggit_taggeditem_items')).order_by('-num_times')[:5]
        return context


class IndexView(ListView):
    template_name="index.html"
    model=Slider 
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['Sliders']=Slider.objects.all()
        context['Abouts']=About.objects.first()
        context['Services']=Service.objects.all()
        context['Blogs']=Blog.objects.all()
        return context

    # context_object_name='Sliders'
    # queryset=Slider.objects.all()





class AboutView(ListView):
    template_name="abouts.html"
    context_object_name='Abouts'
    queryset=About.objects.first()




class ServicesView(ListView):
    template_name="service.html"
    context_object_name='Services'
    queryset=Service.objects.all()



class BlogsView(BaseView,ListView):
    template_name="blogs.html"
    context_object_name='Blogs'
    queryset=Blog.objects.all()
    paginate_by=2
    


class BlogDetailView(BaseView,DetailView):
    template_name="blog-details.html"
    model=Blog
    context_object_name='Blogs'
    slag_url_kwarg='slug'

    def get_object(self, queryset=None):
        obj= super().get_object(queryset=queryset)
        obj.views+=1
        obj.save()
        return obj
    

class BlogSearchView(BaseView,ListView):
    template_name='blog-search.html'
    model=Blog
    context_object_name='Blogs'
    paginate_by=2
    def get_queryset(self):
        query= self.request.GET.get('q')
        if query:
            return Blog.objects.filter(title__icontains=query)
        return Blog.objects.none()



class CategoryDetailView(BaseView,ListView):
    template_name="category-details.html"
    model=Blog
    context_object_name='Blogs'
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category=Category.objects.get(slug=slug)
        return Blog.objects.filter(category=category)

    

class ContactView(TemplateView):
    template_name="contact.html"
    def post(self,request,*args,**kwargs):
        fullName=request.POST.get('fullName')
        phoneNumber=request.POST.get('phoneNumber')
        email=request.POST.get('email')
        message=request.POST.get('message')
        try:
            send_mail(
            f'{fullName} tarafından yeni bir mesaj var',
            f'Mesaj: {message}\n Telefon:{phoneNumber}\n Email:{email}',
            'fidanonur834@gmail.com',
            ['onnurfiddan@gmail.com'],
            fail_silently=False,
            )
            messages.success(request,'Mesajınız başarıyla gönderildi')
        except Exception as e:
            messages.error(request,f'Mesajınız gönderilemedi! {e}')
        
        return HttpResponseRedirect(reverse('contact'))
    

class PageDetailView(BaseView,DetailView):
    template_name='page-details.html'
    model=Page
    context_object_name='Pages'
    slug_url_kwarg='slug'
    