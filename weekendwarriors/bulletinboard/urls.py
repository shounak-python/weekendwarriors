from django.urls import path
from . import views

app_name = "bulletinboard"
urlpatterns = [
    path("", views.bulletinlist, name="bulletinlist"),
    path("<int:pk>", views.bulletindetail, name="bulletindetail"),
]
