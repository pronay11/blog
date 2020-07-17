from django.contrib import admin

from .models import Post, Author,Category
class PostAdmin(admin.ModelAdmin):
    List_display=['tittle','description','created_dt']

class AuthorAdmin(admin.ModelAdmin):
    List_display=['name']    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Author,AuthorAdmin)

