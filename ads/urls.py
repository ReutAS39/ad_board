from django.urls import path, include

from users.views import UserRegister
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CategoryList

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<slug:post_slug>/', PostDetail.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('post/<slug:post_slug>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('post/<slug:post_slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('category/<slug:category_slug>/', CategoryList.as_view(), name='category'),
    #path('login/', PostDelete.as_view(), name='login'),
    #path('register/', UserRegister.as_view(), name='register'),
]