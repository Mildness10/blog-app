from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'list.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.published.all()
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(PostListView, self).get_context_data(*args, **kwargs)
    #     context["posts"] = self.get_queryset()
    #     return context
        
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["posts"] = self.get_queryset()
        return context