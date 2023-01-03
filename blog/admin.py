from django.contrib import admin
from blog import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'discription', 'url', 'add_date',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5

    
    class Media():
        js = ('https://cdn.tiny.cloud/1/u0gx9ps7so1rrlpyxml8v0tl6qktv053onnfgmsigu7nf0ko/tinymce/6/tinymce.min.js', 'js/script.js',)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)