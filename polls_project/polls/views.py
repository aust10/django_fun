from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, your at the polls index!")