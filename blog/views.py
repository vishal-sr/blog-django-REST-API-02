from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Blog
# Create your views here.


@api_view(['GET'])
def blog_summary(request):
    blogs = {}
    for blog in Blog.objects.all():
        blogs[blog.id] = blog.__str__()

    return Response(blogs)


@api_view(['POST'])
def add_blog(request):
    if request.method == "POST":
        pass
    pass
