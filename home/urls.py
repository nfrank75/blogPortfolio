from django.urls import path
from .views import index, contact, about, thanks, projects, blog, blogPost, category, categories, search

urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('thanks', thanks, name="thanks"),
    path('projects', projects, name="projects"),
    path('blog', blog, name="blog"),
    path('blogpost/<str:slug>', blogPost, name="blogPost"),
    path('category/<str:category>', category, name="category"),
    path('categories', categories, name="categories"),
    path('search', search, name="search"),
]
