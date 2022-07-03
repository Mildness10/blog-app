from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail')
]
urlpatterns += staticfiles_urlpatterns()
