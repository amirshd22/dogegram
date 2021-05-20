from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView , name="apiOverView"),
    
    path('posts/', views.getPosts , name="getPosts"),
    path('post-details/<str:pk>/', views.getPostDetails , name="getPostsDetails"),
    path('create-post/', views.createPost , name="createPost"),
    path('like-post/', views.likePost , name="likePost"),
    path('edit-post/<str:pk>/', views.editPost , name="editPost"),
    path('delete-post/<str:pk>/', views.deletePost , name="deletePost"),
    
    path('edit-comment/<str:pk>/', views.editComment , name="editComment"),
    path('delete-comment/<str:pk>/', views.deleteComment , name="deleteComment"),

]