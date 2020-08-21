from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blog(request):
    blogs = Blog.objects
    return render(request, 'blog/blog.html', {'blogs':blogs})

def details(request,blog_id):
    blogdetails = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/blogdetail.html', {'blogdetails':blogdetails})