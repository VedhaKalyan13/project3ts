from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'input.html')

class Add(View):
    def get(self, request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        i = int(x)
        j = int(y)
        k = i + j
        res = HttpResponse("The Sum is:"+str(k))
        return res

class Sub(View):
    def get(self, request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        i = int(x)
        j = int(y)
        k = i - j
        res = HttpResponse("The Sum is:"+str(k))
        return res

class Mul(View):
    def get(self, request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        i = int(x)
        j = int(y)
        k = i * j
        res = HttpResponse("The Sum is:"+str(k))
        return res
class Div(View):
    def get(self, request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        i = int(x)
        j = int(y)
        k = i / j
        res = HttpResponse("The Sum is:"+str(k))
        return res