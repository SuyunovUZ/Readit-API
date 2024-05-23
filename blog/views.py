from rest_framework import generics, viewsets
from .models import (Category,
                     Comment,
                     Post,
                     HappyClients,
                     Author,
                     About,
                     Tag)

from .serializers import (AuthorSerializer,
                          AboutSerializer,
                          CategorySerializer,
                          CommentSerializer,
                          HappyClientsSerializer,
                          PostSerializer,
                          TagSerializer)


class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')
        if q:
            return Post.objects.filter(title__icontains=q)
        if tag:
            return Post.objects.filter(tags__name__icontains=tag)
        if category:
            return Post.objects.filter(category__name__icontains=category)
        else:
            return Post.objects.all()


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class HappyClientsAPIView(generics.ListAPIView):
    queryset = HappyClients.objects.all()
    serializer_class = HappyClientsSerializer


class HomeAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:9]
    serializer_class = PostSerializer


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RecentBlogsAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:3]
    serializer_class = PostSerializer
