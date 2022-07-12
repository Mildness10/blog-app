from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class RecentPostFeed(Feed):
    title = 'Techvilla Blog'
    link = reverse_lazy('blog:post_list')
    description = 'Recent posts of Techvilla Blog'
    
    def items(self):
        return Post.published.all()[:3]
    
    def items_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords(item.body, 20)