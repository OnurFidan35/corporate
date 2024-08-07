from django.urls import path
from .views import AboutView, BlogsView, CategoryDetailView, ContactView, IndexView, ServicesView,BlogDetailView,BlogSearchView,PageDetailView


urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('abouts',AboutView.as_view(),name='abouts'),
    path('services',ServicesView.as_view(),name='services'),
    path('blogs',BlogsView.as_view(),name='blogs'),
    path('blogs/<slug:slug>',BlogDetailView.as_view(),name='blog-detail'),
    path('categories/<slug:slug>',CategoryDetailView.as_view(),name='category-detail'),
    path('contact',ContactView.as_view(),name='contact'),
    path('search',BlogSearchView.as_view(),name='blog-search'),
    path('pages/<slug:slug>/',PageDetailView.as_view(),name='page-detail'),
]
 
