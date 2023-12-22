from django.urls import path
from . import views
from .views import blog_detail

app_name = 'FocalNest'

urlpatterns = [
    path('', views.home, name='home'),
    path('thank-you', views.thankyou, name='thankyou'),
    path('something-went-wrong', views.something_went_wrong, name='something_went_wrong'),
    path('blog', views.blog, name='blog'),
    path('blog/<slug:Title_url>/', views.blog_detail, name='blog_detail'),
    path('service', views.service, name='service'),
    path('service/<slug:Title_url>/', views.service_detail, name='service_detail'),
    path('gallery', views.gallery, name='gallery'),
]
 