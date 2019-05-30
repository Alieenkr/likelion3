from django.shortcuts import render , redirect, get_object_or_404
from .models import Blog, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html',{'blog_post':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    if request.FILES:
        blog.blog_image = request.FILES['blog_image']
    blog.save()

    return redirect('home')


def read(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'read.html', {'blog_post' : blog})

def update(request, blog_id):
    update_post = get_object_or_404(Blog, pk=blog_id)
    update_post.title = request.POST['title']
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('/read/' + str(update_post.id))

def renew(request, blog_id):
    renew_post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'renew.html', {'renew':renew_post})

def delete(request, blog_id):
    delete_post = get_object_or_404(Blog, pk=blog_id)
    delete_post.delete()
    return redirect('home')

def create_c(request, blog_id):
  comment = Comment()
  comment.username = request.POST['comment_username']
  comment.body = request.POST['comment_body']
  comment.pub_date = timezone.datetime.now()
  comment.blog = get_object_or_404(Blog, pk=blog_id)
  comment.save()

  return redirect('read', blog_id=blog_id)