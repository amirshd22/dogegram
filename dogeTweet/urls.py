from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView , name="apiOverView"),
    
    path('tweets/', views.getTweets , name="getTweets"),
    path('tweet-details/<str:pk>/', views.getTweetsDetails , name="getTweetsDetails"),
    path('create-tweet/', views.createTweet , name="createTweet"),
    path('like-tweet/', views.tweetUpvote , name="tweetUpvote"),
    path('edit-tweet/<str:pk>/', views.editTweet , name="editTweet"),
    path('delete-tweet/<str:pk>/', views.deleteTweet , name="deleteTweet"),
    
    path('edit-comment/<str:pk>/', views.editComment , name="editComment"),
    path('delete-comment/<str:pk>/', views.deleteComment , name="deleteComment"),

]