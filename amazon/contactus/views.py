from django.shortcuts import render

# Create your views here.
def contactuspage(request):
    return render(request,"contactus/contactuspage.html")