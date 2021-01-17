"""rcw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from rcw.AllUser.all_user import AllInfo
from rcw.Position.position import Position
from rcw.User.jian_li import JianLi
from rcw.User.user import UserInfo
from rcw.views import Register, FindpwdView, AuthView, AuthViewLoginOut

urlpatterns = [
    path('api/admin', admin.site.urls),
    path('login', AuthView.as_view()),
    path('logout', AuthViewLoginOut.as_view()),

    path('api/api-auth', include('rest_framework.urls')),
    # path('login/', obtain_jwt_token), # jwt 登录接口
    # path('login/', AuthView.as_view()), # jwt 登录接口
    path('api/token/refresh', refresh_jwt_token, name='token_refresh'),  # jwt 刷新token接口

    path('register', Register.as_view()),
    path('api/repeat_pwd', FindpwdView.as_view()),
    path('userinfo', UserInfo.as_view()),
    path('jian', JianLi.as_view()),

    path('position', Position.as_view()),
    # re_path(r'^all_user/$', AllInfo.as_view()),
    path('all_user', AllInfo.as_view())

]
