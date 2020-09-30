"""capstone URL Configuration

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
from django.urls import path, include
#from home.views import home_view
#from parking.views import parking_lot

urlpatterns = [
    path('', include("home.urls")),
    #    path('blog/', include("blog.urls")),
    #    path('workdb/', include("workdb.urls")),
    #    path('learning/', include("learn.urls")),
    #    path('parking/', include("parking.urls")),
    path('orm/', include("orm.urls")),
    #    path('fbv_cbv/', include("fbv_cbv.urls")),
    path('rest/', include("rest.urls")),
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    #    path('table/', include("table.urls")),
]
