from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.validators import EmailValidator
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'snippet/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6     # This is for number of post per page

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            return Post.objects.filter(Q(title__icontains=query) |
                                       Q(subtitle__icontains=query) |
                                       Q(introduction__icontains=query) |
                                       Q(content1__icontains=query) |
                                       Q(code__icontains=query) |
                                       Q(content2__icontains=query) |
                                       Q(author__first_name__icontains=query) |
                                       Q(author__last_name__icontains=query)).order_by("-date_posted")
        return Post.objects.all().order_by("-date_posted")

class UserPostListView(ListView):
    model = Post
    template_name = 'snippet/user_posts.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6     # This is for number of post per page

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'introduction', 'content1', 'code', 'content2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'introduction', 'content1', 'code', 'content2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

