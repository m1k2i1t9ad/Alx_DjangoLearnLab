from django.shortcuts import render, redirect,get_object_or_404  # Import render and redirect functions
from django.contrib.auth import login, authenticate  # Import login and authenticate methods
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .forms import CustomUserCreationForm  # Import the custom user creation form

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# View for user registration
def register(request):
    if request.method == 'POST':  # Check if the request is a POST
        form = CustomUserCreationForm(request.POST)  # Create a form instance with the submitted data
        if form.is_valid():  # Check if the form is valid
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log in the user after registration
            return redirect('profile')  # Redirect to the profile page
    else:
        form = CustomUserCreationForm()  # Create a blank form for GET requests
    return render(request, 'blog/register.html', {'form': form})  # Render the registration template

# View for user profile
@login_required  # Ensure that the user is logged in to access this view
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})  # Render the profile template with user 



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


