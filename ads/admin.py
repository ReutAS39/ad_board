from django.contrib import admin

from ads.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'article', 'category')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
