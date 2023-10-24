
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from thrott import views

router = DefaultRouter()

router.register('teacherappi',views.TeacherModelViewApi,basename='teacher')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]
