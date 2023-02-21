# from .import views
# from django.urls import path
# urlpatterns=[
#     path('',views.showhello,name="hii"),
# ]
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('index',views.index, name="index/"),
    path('index3',views.index3, name="index3/"),
    path('showMessage',views.showMessage, name="showMessage")
    ]