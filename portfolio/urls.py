from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('projects/', views.project, name='project'),
    #path('blog/', views.blog_list, name='blog_list'),
    #path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    #path('certifications/', views.certifications_view, name='certifications'),
    path('resume/', views.resume_view, name='resume'),
]
