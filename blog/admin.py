from django.contrib import admin

# Register your models here.
from .models import Post, Category, About



class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields=('title','content')
    list_filter=('category','created_at')
                   
admin.site.register(Post,PostAdmin)
admin.site.register(Category) 
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['content']