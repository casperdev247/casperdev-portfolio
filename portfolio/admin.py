from django.contrib import admin
from .models import ContactMessage, Project, Tag, BlogPost


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('submitted_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):  # ✅ Changed name
    list_display = ('title', 'project', 'posted_at')
    search_fields = ('title', 'project', 'description')
    list_filter = ('posted_at',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):  # ✅ Changed name
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'tags')
