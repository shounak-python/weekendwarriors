from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthorDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """


class AuthorListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class AuthorCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        object = form.save(commit=False)
        object.author = self.request.user
        object.save()
        return super(AuthorCreateView, self).form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):

        qs = super(AuthorUpdateView, self).get_queryset()
        return qs.filter(author=self.request.user)


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):

        qs = super(AuthorDeleteView, self).get_queryset()
        return qs.filter(author=self.request.user)
