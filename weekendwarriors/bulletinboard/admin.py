from django.contrib import admin
from bulletinboard.models import Bulletin

# Register your models here.
class BulletinAdmin(admin.ModelAdmin):
    list_display = ("title", "created_on", "updated_on", "subtitle")

admin.site.register(Bulletin, BulletinAdmin)
