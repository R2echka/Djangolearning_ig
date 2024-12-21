from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import Blog
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class BlogList(ListView):
    model = Blog
    template_name = 'blogs/posts.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_publicated=True)


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blogs/post.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object

class BlogCreate(CreateView):
    model = Blog
    template_name = 'blogs/post_form.html'
    fields = ['title', 'text', 'preview']
    success_url = reverse_lazy('blogs:blog')

class BlogUpdate(UpdateView):
    model = Blog
    template_name = 'blogs/post_form.html'
    fields = ['title', 'text', 'preview']
    success_url = reverse_lazy('blogs:post')
    def get_success_url(self):
        return reverse('blogs:post', args=[self.kwargs.get('pk')])

class BlogDelete(DeleteView):
    model = Blog
    template_name = 'blogs/post_delete.html'
    success_url = reverse_lazy('blogs:blog')
