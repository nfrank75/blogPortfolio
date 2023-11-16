from django.contrib import admin
from home.models import Blog, Contact

admin.site.site_header = "Nfrank Portfolio Config Django"
admin.site.index_title = "Nfrank Portfolio Config Django Administration"


class BlogAdmin(admin.ModelAdmin): 
    list_display = (
        "title",
        "meta",
        "content",
        "blog_img",
        'blog_url',
        'category',
        'slug'
        )
    ordering = ('-created_at',)

    fields = (
        "title",
        "meta",
        "content",
        "blog_img",
        'blog_url',
        'category',
        'slug'
        )

class ContactAdmin(admin.ModelAdmin): 
    list_display = (
        "contact_name",
        "email",
        "phone",
        "message",
    )
    
    fields = (
        "contact_name",
        "email",
        "phone",
        "message",
    )
    
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)