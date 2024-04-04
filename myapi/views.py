from rest_framework import generics
from rest_framework.generics import RetrieveAPIView

from .models import Blog,Comment
from .serializer import BlogSerializer,Getblogserializer,Replieserializer,Commentserializer
from rest_framework import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = Getblogserializer
    lookup_url_kwarg = 'pk'  


class Addcomments(APIView):
    def post(self, request):
        try:
            data =request.data
            serializer = Commentserializer(data=data)
            if serializer.is_valid():
                user=serializer.validated_data
                done=Comment(
                blog=user.get('blog'),
                author=user.get('author'),
                content=user.get('content'),
                )
                done.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                errors = serializer.errors
                print("Serializer Errors:", errors)
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(request, *args, **kwargs):
        try:
            blog_id = kwargs.get('id')
            blog_instance = Blog.objects.get(id=blog_id)
            all_comments = Comment.objects.filter(blog=blog_instance)
            serializer = Commentserializer(all_comments, many=True)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
            
class Replies(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = Replieserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                errors = serializer.errors
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)