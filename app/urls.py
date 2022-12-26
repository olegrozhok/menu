from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('main/', views.menu, name='main'),
    path('submenu1/', views.submenu1, name='submenu1'),
    path('submenu2/', views.submenu2, name='submenu2'),
    path('submenu3/', views.submenu3, name='submenu3'),
]
