from django.contrib import admin
from members.models import Member, Foot, Proficiency, FieldPosition

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "preferred_foot", "preferred_field_position", "football_proficiency")

admin.site.register(Member, MemberAdmin)
admin.site.register(Foot)
admin.site.register(Proficiency)
admin.site.register(FieldPosition)
