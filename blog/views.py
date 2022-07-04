from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'list.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.published.all()
        
    
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'detail.html'
    
#     def get_context_data(self, *args, **kwargs):
#         context = super(PostDetailView, self).get_context_data(*args, **kwargs)
#         context["posts"] = self.get_queryset()
#         return context

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'detail.html', {'post':post})
    
    

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = ''
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url  = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} has shared the post '{post.title}' with you."
            message = f"You can access and read '{post.title}' at {post_url}. {cd['name']}'s comment to you on this post is, {cd['comments']}"
            send_mail(subject, message, 'mildnessozy45@gmail.com', [cd['receiver']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'post':post, 'form':form, 'sent':sent})
