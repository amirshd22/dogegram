from django.shortcuts import render
from .models import Tweets,TweetComment,UpVoteTweet
from  .serializers import TweetsSerializer,TweetCommentSerializer,TweetLikeSerializer
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, status


# Create your views here.


@api_view(["GET"])
def apiOverView(request):
    api_urls= {
        "Get Tweets":"/tweets/",
        "Get tweet Details": "/tweet-details/",
        "Create tweet": "/create-tweet/",
        "Like tweet": "/like-tweet/",
        "Edit tweet": "/edit-tweet/",
        "Delete tweet": "/delete-tweet/",
        "Edit Comment": "/edit-comment/",
        "Delete Comment": "/delete-comment/"
    }
    return Response(api_urls)


@api_view(["GET"])
def getTweets(request):
    query = request.query_params.get('q')
    if query == None:
        query = ""
    tweet = Tweets.objects.filter(Q(content__icontains=query)|Q(title__icontains=query))
    serializer = TweetsSerializer(tweet, many=True)
    return Response(serializer.data)


def getTweetsDetails(request,pk):
    try:
        tweet = Tweets.objects.get(id=pk)
        serializer = TweetsSerializer(tweet, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["POST"])
def createTweet(request):
    data = request.data
    user = request.user
    isComment = data['isComment']
    if isComment:
        tweet = Tweets.objects.get(id=data['tweetId'])
        comment = TweetComment.objects.create(
            content=data['content'],
            tweet=tweet,
            user = user
        )
        comment.save()
        serializer = TweetCommentSerializer(comment, many=False)
        return Response(serializer.data)
    else:
        tweet = Tweets.objects.create(
        content= data['content'],
        title = data['title'],
        user = user
        )
        tweet.save()
        serializer= TweetsSerializer(tweet, many=False)
        return Response(serializer.data)

@api_view(['POST'])
def tweetUpvote(request):
    data = request.data
    user = request.user

    tweetid = data["tweetId"]

    commentId = data["commentId"]
    tweet = Tweets.objects.get(id=tweetid)
    if commentId:
        comment = TweetComment.objects.get(id=commentId)
        like,created = UpVoteTweet.objects.get_or_create(tweet=tweet,comment=comment,value=1)
        if not created:
            like.delete()
        else:
            like.save()
    else:
        like, created = UpVoteTweet.objects.get_or_create(tweet=tweet,user=user,value=1)
        if not created:
            like.delete()
        else:
            like.save()
    serializer = TweetLikeSerializer(tweet, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def editTweet(request,pk):
    data =  request.data
    user = request.user
    try:
        tweet = Tweets.objects.get(id=pk)
        if user == tweet.user :
            tweet.content = data["content"]
            tweet.title = data["title"]
            tweet.save()
            serializer = TweetsSerializer(tweet,many=False)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["DELETE"])
def deleteTweet(request,pk):
    user =  request.user
    try: 
        tweet = Tweets.objects.get(id=pk)
        if tweet.user == request.user:
            tweet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def editComment(request,pk):
    data = request.data
    try:
        comment = TweetComment.objects.get(id=pk)
        if comment.user == request.user:
            comment.conetent = data["content"]
            serializer = TweetCommentSerializer(comment, many=False)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteComment(request, pk):
    try:
        comment= TweetComment.objects.get(id=pk)
        if comment.user == request.user:
            serializer = TweetCommentSerializer(comment,many=False)
            comment.delete()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)
