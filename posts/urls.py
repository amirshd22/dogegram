from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView , name="apiOverView"),
    
    path('posts/', views.getPosts , name="getPosts"),
    path('post-details/', views.getPostDetails , name="getPostsDetails"),
    path('create-post/', views.createPost , name="createPost"),
    path('like-post/', views.likePost , name="likePost"),
    path('edit-post/', views.editPost , name="editPost"),
    path('delete-post', views.deletePost , name="deletePost"),
    
    path('edit-comment', views.editComment , name="editComment"),
    path('delete-comment', views.deleteComment , name="deleteComment"),

]