from django.urls import path
from .views import *
urlpatterns = [

    path('all_blog/',BlogListView.as_view()),
    path('apiblog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('addcommenst/',Addcomments.as_view()),
    path('comments/<int:id>/', Addcomments.as_view(), name='get_comments'),
    path('replies/',Replies.as_view()),

]