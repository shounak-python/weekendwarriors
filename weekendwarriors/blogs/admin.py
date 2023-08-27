from django.contrib import admin
from blogs.models import Blogs

# Register your models here.
class BlogsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "author",
        "created_at",
        "updated_at",
    )

admin.site.register(Blogs, BlogsAdmin)