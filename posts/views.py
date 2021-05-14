from django.shortcuts import render
from .models import Post,PostComment,PostLike
from .serializers import PostCommentSerializer,PostLikeSerializer,PostSerializers
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status


@api_view(["GET"])
def apiOverView(request):
    api_urls= {
        "Get Posts":"/posts/",
        "Get Post Details": "/post-details/",
        "Create Post": "/create-post/",
        "Like Post": "/like-post/",
        "Edit Post": "/edit-post/",
        "Delete Post": "/delete-post/",
        "Edit Comment": "/edit-comment/",
        "Delete Comment": "/delete-comment/"
    }
    return Response(api_urls)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getPosts(request):
    query = request.query_params.get('q')
    if query == None:
        query = ""
    posts = Post.objects.filter(Q(content__icontains=query)|Q(title__icontains=query))
    #TODO: Add infinite loop to the project
    serializer = PostSerializers(posts, many=True)
    return Response(serializers.data)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def createPost(request):
    data = request.data
    user = request.user
    isComment = data["isComment"]
    if isComment:
        post = Post.objects.get(id=data["postId"])
        comment = PostComment.objects.create(
            user=user,
            content = data['content'],
            post=post
        )
        comment.save()
        serializer = PostCommentSerializer(comment, many=False)
        return Response(serializer.data)

    else:
        tag = data["tag"]
        image = data["image"]
        description = data["description"]
        title = data["title"]
        post = Post.objects.create(
            user=user,
            description=description,
            title=title,
            image=image,
            tag=tag
        )
        post.save()
        serializer= PostSerializers(post,many=False)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def likePost(request):
    data = request.data
    user = request.user

    postId = data["postId"]

    commentId = data["commentId"]

    post = Post.objects.get(id=postId)
    if commentId:
        comment = PostComment.objects.get(id=commentId)
        like,created = PostLike.objects.get_or_create(post=post,comment=comment,value=1)
        if not created:
            like.delete()
        else:
            like.save()
    else:
        like, created = PostLike.objects.get_or_create(post=post,user=user,value=1)
        if not created:
            like.delete()
        else:
            like.save()
    serializer = PostLikeSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def editPost(request, pk):
    data = request.data
    try:
        post = Post.objects.get(id=pk)
        if post.user == request.user:
            post.title=data['title']
            post.image=data['image']
            post.description=data['description']
            post.tag=data['tag']
            post.save()
            serializer = PostSerializers(post,many=False)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deletePost(request, pk):
    try:
        post= Post.objects.get(id=pk)
        if post.user == request.user:
            post.delete()
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
        comment = PostComment.objects.get(id=pk)
        if comment.user == request.user:
            comment.conetent = data["content"]
            serializer = PostCommentSerializer(comment, many=False)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteComment(request, pk):
    try:
        comment= PostComment.objects.get(id=pk)
        if comment.user == request.user:
            serializer = PostCommentSerializer(comment,many=False)
            comment.delete()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getPostDetails(request,pk):
    try:
        post = Post.objects.get(id=pk)
        serializer= PostSerializers(post,many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)
