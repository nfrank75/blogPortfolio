from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.db.models import Q

from .models import Blog, Contact
import random


def index(request):
    blogs = Blog.objects.all()
    if len(blogs) > 3:
        random_blogs = random.sample(list(blogs), 3)
    # random_blogs = random.sample(list(blogs), 3) # pour afficher 3 blogs sur la page d'acceuil

        context = {'random_blogs': random_blogs}
        return render(request, 'index.html', context)
    else :
        context = {'blogs': blogs}
        return render(request, 'index.html', context )

def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if contact_name and email and phone and message :
            contact = Contact(
                contact=contact_name, 
                email=email,
                phone=phone,
                message=message
                )
            contact.save()

    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 3) # paginer les blogs en 3 
    page = request.GET.get('page') # recuperer le numero de la page
    blogs = paginator.get_page(page)
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def blogPost(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        context = {'blog': blog}
        return render(request, 'blogpost.html', context)
    except Blog.DoesNotExist:
        context = {'messages': 'Blog Post not found'}
        return render(request, "404.html", context, status=404)

def category(request, category):
    category_posts = Blog.objects.filter(category=category)
    if not category_posts:
        message = f"No Posts on this category: {category}"
        return render(request, "category.html", {'message': message})
    paginator = Paginator(category_posts, 3)
    page = request.GET.get('page')
    category_posts = paginator.get_page(page)
    return render(request, 'category.html', {"category": category, 'category_posts': category_posts})

def categories(request):
    all_categories = Blog.objects.values('category').distinct().order_by('category')
    return render(request, 'categories.html', {'all_categories': all_categories})


def search(request):
    query = request.GET.get('q')
    if query:
        query_list = query.split()
        results = Blog.objects.none()
        for word in query_list:
            results = results | Blog.objects.filter(Q(title__contains=word)) | (Q(content__contains=word)).order_by('-created_by')
        paginator = Paginator(results, 3)
        page = request.GET.get('page')
        results = paginator.get_page(page)
        if len(results) == 0:
            messages = 'sorry, no result found for your search query.'
        else:
            messages = ''
        return render(request, 'search.html', {'results': results, 'query': query, 'message': message})
    else: 
        return render(request, 'search.html')
    
