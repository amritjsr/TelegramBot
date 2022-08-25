from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def hello_world(request):
    if str(request.method).upper() == 'GET':
        return HttpResponse('<h2>GET Request .... Greetings from India !!!!!!!!</h2>')
    elif str(request.method).upper() == 'POST':
        # print(request.POST)
        print(request.body.decode('UTF-8'))
        return HttpResponse('<h2>POST Request Greetings from India !!!!!!!!</h2>')