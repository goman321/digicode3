from django.contrib import admin
from .models import Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "jpublish", "list_category" ,"is_active")
    list_filter = (
        "is_active", "jpublish"
    )
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = [
        "-is_active", "-jpublish"
    ]

    def list_category(self, obj):
        return ", ".join(str(category) for category in obj.category.all())
    list_category.short_description = "دسته‌بندی"

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)