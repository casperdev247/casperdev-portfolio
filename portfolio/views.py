from .models import ContactMessage
from .models import BlogPost
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import ContactForm
from .models import ContactMessage, Project, Tag


def index(request):
    projects = Project.objects.all()

    return render(request, 'portfolio/index.html', {
        'featured_projects': projects,
    })


def about_view(request):
    tech_stack = [
        "Python", "Django", "TailwindCSS", "JavaScript",
        "WebSocket", "HTML5", "Git", "PostgreSQL"
    ]
    return render(request, 'portfolio/about.html', {'tech_stack': tech_stack})


def contact_view(request):
    return render(request, 'portfolio/contact.html', {})


def project(request):
    selected_tag = request.GET.get('tag')
    tags = Tag.objects.all()

    if selected_tag:
        projects = Project.objects.filter(tags__name=selected_tag)
    else:
        projects = Project.objects.all()

    return render(request, 'portfolio/project.html', {
        'projects': projects,
        'tags': tags,
        'selected_tag': selected_tag
    })


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'portfolio/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'post': post})


def certifications_view(request):
    return render(request, 'portfolio/certifications.html')


def resume_view(request):
    return render(request, 'portfolio/resume.html')
