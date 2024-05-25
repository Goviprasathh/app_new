from django.shortcuts import HttpResponse




def user(request):
    return HttpResponse('<h1>Hello</h1>')
