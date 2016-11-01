from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from notgur.forms import CommentForm
from notgur.models import Image
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ImageListView(ListView):
    model = Image
    paginate_by = 5

class ImageCreateView(CreateView):
    model = Image
    fields = ('title', 'description', 'picture')
    success_url = reverse_lazy("image_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        return super().form_valid(form)

class ImageUpdateView(UpdateView):
    model = Image
    fields = ('title', 'description')
    success_url = reverse_lazy("image_list_view")

class ImageDetailView(DetailView):
    model = Image

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

class CommentFormView(FormView):
    form_class = CommentForm
    success_url = reverse_lazy("image_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        instance.image = Image.objects.get(id=self.kwargs["pk"])
        instance.save()
        return super().form_valid(form)

class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy("image_list_view")
    form_class = UserCreationForm

class ProfileView(ListView):
    template_name = "profile.html"
    model = Image
    paginate_by = 5

    def get_queryset(self):
        return Image.objects.filter(created_user=self.request.user)
