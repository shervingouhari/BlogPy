from django.shortcuts import get_object_or_404, get_list_or_404
from django.utils.http import urlencode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ArticleSerializer
from .models import Article
from .permissions import IsOwnerOrReadOnly


class ArticleAPI(APIView):
    def get(self, request):
        if request.GET:
            kwargs = dict(
                q.split('=')
                for q in urlencode(request.GET, doseq=True).split('&')
            )
            articles = get_list_or_404(Article, **kwargs)
        else:
            articles = get_list_or_404(Article)
        return Response(
            self.serializer_class(instance=articles, many=True).data
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.check_object_permissions(request, serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = self.serializer_class(
            instance=article, data=request.data, partial=True
        )
        if serializer.is_valid():
            self.check_object_permissions(request, article)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        self.check_object_permissions(request, article)
        article.delete()
        return Response(
            {'detail': 'Article deleted successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ArticleSerializer
