from django.urls import path
from . import views 

urlpatterns=[
  path('',views.index,name='index'),
  path('wishlist',views.wishlist, name="wishlist"),
  path('login',views.login, name="login"),
  path('register',views.register, name="register"),
  path('about',views.about, name="about"),
  path('shipping',views.shipping, name="shipping"),
  path('contact',views.contact, name="contact"),
  path('care',views.care, name="care"),
  path('hold',views.hold, name="hold"),
  path('kitchen',views.kitchen, name="kitchen"),
  path('offer',views.offer, name="offer"),
  path('single',views.single, name="single")
]