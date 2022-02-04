from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import  Paginator


from blog.models import Blog, Comment_blog
from .forms import CommentBlogForm



# ---------------------------------------------------------------------------- #
#                                     BLOG                                     #
# ---------------------------------------------------------------------------- #


def blog(request):
    blogs = Blog.objects.all()
    comment_blog = Comment_blog.objects.all()
    paginator = Paginator(blogs, 1)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs': paged_blogs,
        'comment_blog': comment_blog,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    comment_blog = Comment_blog.objects.filter(blog_id=blog_id, status='True')
    comment_blog_count = comment_blog.count()
    context = {
        'blog': blog,
        'comment_blog': comment_blog,
        'comment_blog_count': comment_blog_count,
    }
    return render(request, 'blog/blog-post.html', context)


def comment_blog(request, blog_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentBlogForm(request.POST)
        if form.is_valid():
            data = Comment_blog()
            data.blog_id = blog_id
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(
                request, "Sizning kommentariyangiz qabul qilindi!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
