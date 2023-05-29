# These urls/endpoints will be mapped to our views.
from django.urls import path
from . import views

# URLConf module. Similar to routers in Express. Also need to include this URLConf in the main urls.py (which is in Storefront app). 
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello/html/', views.say_hello_html)
]