from django.http import HttpResponse

def about(request):
    return HttpResponse("Esta es la pagina About")
