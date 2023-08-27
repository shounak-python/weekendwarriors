from django.urls import path, reverse_lazy
from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.BlogListView.as_view(), name="blogs_list"),
    path("<int:pk>", views.BlogDetailView.as_view(), name="blogs_detail"),
    path(
        "create",
        views.BlogCreateView.as_view(success_url=reverse_lazy("blogs:blogs_list")),
        name="blogs_create",
    ),
    path(
        "<int:pk>/update",
        views.BlogUpdateView.as_view(success_url=reverse_lazy("blogs:blogs_list")),
        name="blogs_update",
    ),
    path(
        "<int:pk>/delete",
        views.BlogDeleteView.as_view(success_url=reverse_lazy("blogs:blogs_list")),
        name="blogs_delete",
    ),
    ]
