
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name="home"),
    path('gallery/', views.gallery,name="gallery"),
    path('form/', views.form,name="form"),
    path('table/', views.table,name="table"),
    path('login/', views.login,name="login"),
    path('', views.register,name="register"),
]
