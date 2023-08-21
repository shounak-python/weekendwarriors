from django.urls import path
from . import views

app_name = "members"
urlpatterns = [
    path("", views.memberlist, name="memberlist"),
    path("deduct_group/", views.deduct_group, name="deduct_group"),
]