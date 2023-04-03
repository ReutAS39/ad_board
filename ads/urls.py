from django.urls import path, include
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<slug:post_slug>>', PostDetail.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('category/<slug:cat_slug>/', PostList.as_view(), name='category'),
]