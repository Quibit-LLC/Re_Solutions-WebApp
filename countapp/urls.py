from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',index, name='index'),
    path('signup/',signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),
    path('logout',logout,name='logout'),
    path('create_resolution/', create_resolution, name='create_resolution'),
    path('create_contact/',create_contact, name='create_contact'),
    path('resolutions/', resolution, name='resolutions'),
    path('<int:pk>/delete_resolution/', delete_resolution, name='delete_resolution'),
    path('<int:pk>/edit_resolution/', edit_resolution, name='edit_resolution'),
    path('create_article/', create_news_article, name='create_news_article'),
    path('articles/', all_news_articles, name='all_news_articles'),
    path('<int:pk>/article/', news_article_detail, name='news_article_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# add this line to display the media contents