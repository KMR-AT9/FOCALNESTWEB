
from .models import BlogPost, ServicePost

def common_data(request):
    allservices = ServicePost.objects.all()
    allblogs = BlogPost.objects.all().order_by('-id')
    recent_blogs = BlogPost.objects.all().order_by('-id')[:5]
    return {
        'services': allservices,
        'blogs': allblogs,
        'recentblogs': recent_blogs,
    }
