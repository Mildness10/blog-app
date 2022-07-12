from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import PostListView, post_search
from .feeds import RecentPostFeed
from . import views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    # path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('latest/feed/', RecentPostFeed(), name='post_feed'),
    path('search', post_search, name='post_search')
]
urlpatterns += staticfiles_urlpatterns()
