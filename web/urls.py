"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from . import view
from DrakWeb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index),
    path('index/', view.index),
    #the route of executing crawling
    # path('Basic_crawler/', Basic_crawler),
    # path('Teach_crawler/', Teach_crawler),
    # path('Other_crawler/', Other_crawler),
    # path('Service_crawler/', Service_crawler),
    # path('Sex_crawler/', Sex_crawler),
    # path('Virtual_Source_crawler/', Virtual_Source_crawler),
    # path('Material_crawler/', Material_crawler),
    # path('Data_crawler/', Data_crawler),
    # path('Private_crawler/', Private_crawler),
    # path(r'^CVV_crawler/$', CVV_crawler),
    #the route of checking database
    path('Basic/', view.Read_Basic),
    path('Data/', view.Read_Data),
    path('Other/', view.Read_Other),
    path('Sex/', view.Read_Sex),
    path('Virtual_Source/', view.Read_Virtual_Source),
    path('Material/', view.Read_Material),
    path('Service/', view.Read_Service),
    path('Private/', view.Read_Private),
    path('CVV/', view.Read_CVV),
    path('Teach/', view.Read_Teach),
    #the root of user login and logout
    path('login/', view.login),
    path('regist/', view.regist),
    path('logout/', view.logout)
]
