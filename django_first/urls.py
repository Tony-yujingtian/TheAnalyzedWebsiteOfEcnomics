"""django_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from economic import views
urlpatterns = [
    path('', views.main),  #首页
    path('main/', views.pro_main),  #首页
    path('download_list/',views.download_list),#下载分类
    path('download_list/'+'<str:list>/',views.download),#下载列表
    path('download_list/'+'<str:down>/'+'<str:list>',views.download_temp),#下载
    path('analysis/',views.analysis_list),#分析列表
    path('analysis/' + '<str:list>/', views.analysis),  # 分析列表_二级
    path('analysis/' + '<str:list>/'+ '<str:data_list>/'+'<str:method>', views.analysis_method_list)

    # path('index_download/', views.index_download),  #下载列表
    # path('charts/', views.chart),
    # path('analysis/',views.analysis),
    # path('analysis/'+'<str:id>',views.analysis),
    # path('charts/'+'<str:id>', views.chart),
    # path('index_download/'+'<str:id>',views.download_template),   #下载
    # path('mulu/', views.mulu),

]
