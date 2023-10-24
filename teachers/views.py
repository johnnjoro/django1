from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to emobilis")

def about(request):
    return HttpResponse("About emobilis")

def courses(request):
    return HttpResponse("We offer the Following Courses")

def contacts(request):
    return HttpResponse("Feel free to reach us through our social media platforms")

def location(request):
    return HttpResponse("Visit our offices in Westlands")
