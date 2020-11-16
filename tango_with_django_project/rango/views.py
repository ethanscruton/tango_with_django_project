from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!" + '<a href="/rango/about/">\nAbout</a>')

def about(request):
    return HttpResponse("Rango says here is the about page." + '<a href="/rango/index/">\nIndex</a>')


