from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"name": "Juan Esteban"})

def about(request):
    return render(request, "about.html")


from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


    