from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from blog.forms import Comment_detail_Form
from blog.models import Blog, Category_Blog, Tag_Blog, Comment_blog
from home.models import Informations
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)



def blog(request):
    blogs = Blog.objects.all()
    comment_blog = Comment_blog.objects.all()
    paginator = Paginator(blogs, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        'blogs':blogs,
        'comment_blog':comment_blog,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request,id):
    blog = Blog.objects.get(pk=id)
    comment_blog = Comment_blog.objects.filter(blog_id=id, status='True')
    comment_blog_count = comment_blog.count()
    context = {
        'blog':blog,
        'comment_blog':comment_blog,
        'comment_blog_count':comment_blog_count,
    }
    return render(request, 'blog/blog-post.html', context)



def comment_blog(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_detail_Form(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = id
            data.save()
            messages.success(request, "Sizning izohingiz qabul qilindi !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)