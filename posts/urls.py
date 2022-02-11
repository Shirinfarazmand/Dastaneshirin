from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<str:pk>',views.post, name='post'),
    path('register',views.register, name= 'register'),
    path('login',views.login, name= 'login'),
    path('about',views.about, name= 'about'),
    path('contact',views.contact, name='contact'),
    path('logout',views.logout , name='logout'),
    # path('<slug:slug>/', views.post_detail, name='post_detail')


]
