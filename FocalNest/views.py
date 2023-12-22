from django.shortcuts import render, get_object_or_404
from .models import BlogPost, ServicePost, Gallery
from django.shortcuts import render,redirect
from .forms import EnquiryForm
from django.urls import reverse
from django.db import connection


def home(request):
    form = EnquiryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = EnquiryForm()
            return render(request, 'thank-you.html')

    return render(request, 'index.html', {'form': form})

def thankyou(request):
    if request.method == 'POST':
        return render(request, 'thank-you.html')
    else:
        return redirect(reverse('FocalNest:something_went_wrong'))

def something_went_wrong(request):
    return render(request, 'something-went-wrong.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request, Title_url): 
    post = get_object_or_404(BlogPost, Title_url=Title_url)
    more_blogs = BlogPost.objects.exclude(id=post.id)
    latest_posts = BlogPost.objects.exclude(id=post.id).order_by('-id')[:5]
    return render(request, 'blog-detail.html', {'post': post, 'more_posts': more_blogs, 'latest_posts': latest_posts})

def service(request):
    return render(request, 'service.html')

def service_detail(request, Title_url):
    post = get_object_or_404(ServicePost, Title_Url=Title_url)
    galleries = Gallery.objects.filter(service=post)
    more_services = ServicePost.objects.exclude(id=post.id)
    return render(request, 'service-detail.html', {'post': post, 'galleries': galleries, 'more_posts': more_services})

def gallery(request):
    allimages = Gallery.objects.all().order_by('-id')
    return render(request, 'gallery.html', {'images': allimages})
