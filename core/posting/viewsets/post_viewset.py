import os

from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from ..serializers import PostSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..forms import *
from rest_framework.decorators import action


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-created_on')
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    # def create(self, request):
    #     # serializer = PostSerializer(data=request.data)
    #     #
    #     # if serializer.is_valid():
    #     #     image_file = request.FILES.get('image_content')
    #     #
    #     #     if image_file:
    #     #         post_instance = serializer.instance
    #     #         post_instance.image_content = image_file
    #     #         post_instance.save()
    #     #
    #     #     serializer.save(author=request.user)
    #     #
    #     #
    #     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #     if request.method == 'GET':
    #         return render(request, 'base.html')
    #     elif request.method == 'POST':
    #         file = request.FILES.get('image_content')
    #
    #         new_post = Post(author=request.user, text_content=request.POST.get('text_content'), image_content=file)
    #         new_post.save()
    #         return Redi

    @classmethod
    @action(detail=False, methods=['POST'])
    def create_post(self, request):

        if request.method == 'GET':
            return render(request, 'base.html')

        elif request.method == 'POST':
            text_content = request.POST.get('text_content')
            files = request.FILES.getlist('file_content')
            data = {'text_content': text_content}
            serializer = PostSerializer(data=data)

            if serializer.is_valid():
                post = serializer.save(author=request.user)
                if files:
                    for f in files:
                        PostFile.objects.create(post=post, arq_content=f)

                return redirect('feed')
            else:
                return render(request, 'error.html', {'errors': serializer.errors})


    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            post = get_object_or_404(self.queryset, **kwargs)
            serializer = PostSerializer(post)
            return Response(serializer.data)

    # def destroy(self, request, slug):
    #     if request.method == 'POST':
    #         post = Post.objects.get(slug=slug)
    #         post.delete()
    #         return redirect('feed')

    @classmethod
    @action(detail=True, methods=['post'])    
    def delete_post(self, request, slug):
        if request.method == 'POST':
            post = Post.objects.get(slug=slug)
            post.delete()
            return redirect('feed')
        return render(request, 'feed.html')

    @action(detail=True, methods=['post'])
    def update_post(self, request, slug=None):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('feed')
        return render(request, 'feed.html')

    @action(detail=True, methods=['post'])
    def delete_file_post(self, request, id=None):
        if request.method == 'POST':
            image = PostFile.objects.get()


    def create_file_post(self,request, sla):
        if request.method == 'POST':
            img = PostFile.object.create(post=post_id, arq_content=sla)


@login_required
def post_list(request):
    feed = PostViewSet.as_view({'get': 'list'})(request).data
    comments = Comment.objects.all().order_by('created_on')
    return render(request, 'feed.html', {'feed': feed, 'comments': comments, 'user': request.user})


@login_required
def explore_list(request):
    feed = PostViewSet.as_view({'get': 'list'})(request).data
    comments = Comment.objects.all().order_by('created_on')
    return render(request, 'explore.html', {'feed': feed, 'comments': comments, 'user': request.user})
