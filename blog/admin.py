from django.contrib import admin
from .models import (Category,
                     Comment,
                     Post,
                     HappyClients,
                     Author,
                     About,
                     Tag)


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'author')
    search_fields = ['title', 'author']
    filter_horizontal = ['tags']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(HappyClients)
admin.site.register(Comment)
