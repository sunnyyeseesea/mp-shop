"""
URL configuration for django_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py
# from django_shop import views
from django.urls import path, include
from django.contrib import admin
from django.urls import path
# django项目目录下的urls.py，让首页显示打包的index.html文件
from django.views.generic import TemplateView
from django.views.generic import RedirectView
# import student from student

urlpatterns = [
    path('', RedirectView.as_view(url='/static/index.html', permanent=False), name='index'),
    path('admin/', admin.site.urls),
    # path("student/", include("student.urls")), 测试项目，用于初学，已经卸载，可以在sports_shop——backend_war目录下的舍不得_宝贝垃圾桶里面找到
    path("sports_shop_backend_war/",include("sports_shop_backend_war.urls"))
]
