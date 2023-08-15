from django.contrib import admin
from members.models import Member, Foot, Proficiency, FieldPosition, Attendance, Balance

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "preferred_foot",
        "preferred_field_position",
        "football_proficiency",
    )


class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "Nikhil_Kadukar",
        "Rajesh_Sharma",
        "Omkar_Panda",
        "Vinod_Hiwale",
        "Niraj_Gadhe",
        "Ritesh_Chambhare",
        "Jayant_Wani",
        "Neelang_Chaturvedi",
        "Durgesh_Patil",
        "Shanmukha_Vardhan",
        "Rahul_Dhokale",
        "Amod_Narhari",
        "Kunal_Aswale",
        "Sameer_Shewale",
        "Vaibhav_Sonar",
        "Prem_Jadhav",
        "Chirag",
        "Dilip_Mahajan",
        "Vijay_Pal",
        "Shounak_Deshpande",
        "Adwait_Sarnobat",
        "Umesh",
        "Ankit",
        "Satheesh",
        "Varun",
        "Prasad",
        "Vinit",
        "Sahil",
        "Arun",
        "Souvik",
        "Tuahar",
        "Sujit",
        "Shreekant",
    )


class BalanceAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "Nikhil_Kadukar",
        "Rajesh_Sharma",
        "Omkar_Panda",
        "Vinod_Hiwale",
        "Niraj_Gadhe",
        "Ritesh_Chambhare",
        "Jayant_Wani",
        "Neelang_Chaturvedi",
        "Durgesh_Patil",
        "Shanmukha_Vardhan",
        "Rahul_Dhokale",
        "Amod_Narhari",
        "Kunal_Aswale",
        "Sameer_Shewale",
        "Vaibhav_Sonar",
        "Prem_Jadhav",
        "Chirag",
        "Dilip_Mahajan",
        "Vijay_Pal",
        "Shounak_Deshpande",
        "Adwait_Sarnobat",
        "Umesh",
        "Ankit",
        "Satheesh",
        "Varun",
        "Prasad",
        "Vinit",
        "Sahil",
        "Arun",
        "Souvik",
        "Tuahar",
        "Sujit",
        "Shreekant",
    )


admin.site.register(Member, MemberAdmin)
admin.site.register(Foot)
admin.site.register(Proficiency)
admin.site.register(FieldPosition)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Balance, BalanceAdmin)