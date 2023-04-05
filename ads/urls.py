from django.urls import path

from . import views
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CategoryList

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<slug:post_slug>/', PostDetail.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('post/<slug:post_slug>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('post/<slug:post_slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('category/<slug:category_slug>/', CategoryList.as_view(), name='category'),
    path('post/<slug:post_slug>/upload_image', views.upload_image, name='upload_image'),
    path('comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
]