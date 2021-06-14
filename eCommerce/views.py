from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request,"index.html")
def wishlist(request):
  return render(request,"wishlist.html")
def login(request):
  return render(request,"login.html")
def register(request):
  return render(request,"register.html")
def about(request):
  return render(request,"about.html")
def shipping(request):
  return render(request,"shipping.html")
def contact(request):
  return render(request,"contact.html")
def hold(request):
  return render(request,"hold.html")
def kitchen(request):
  return render(request,"kitchen.html")
def offer(request):
  return render(request,"offer.html")
def single(request):
  return render(request,"single.html")
def care(request):
  return render(request,"care.html")