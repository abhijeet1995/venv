from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>polls app under construction</h1>")
