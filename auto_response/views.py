from email import message
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import environ
import json
import requests
# Create your views here.


env = environ.Env()
SAYONAARA_API_KEY = env('SAYONAARA_API_KEY')

@csrf_exempt
def hello_world(request):
    if str(request.method).upper() == 'GET':
        return HttpResponse('<h2>GET Request .... Greetings from India !!!!!!!!</h2>')
    elif str(request.method).upper() == 'POST':
        # print(request.POST)
        print(request.body.decode('UTF-8'))
        return HttpResponse('<h2>POST Request Greetings from India !!!!!!!!</h2>')

@csrf_exempt
def app_root(request):
    if str(request.method).upper() == 'GET':
        return HttpResponse('<h2>GET Request .... <h1>4?4</h1> !!!!!!!!</h2>')
    elif str(request.method).upper() == 'POST':
        # print(request.POST)
        print(request.body.decode('UTF-8'))
        data = json.loads(request.body.decode('UTF-8'))
        if 'text' in data['message'].keys():
            user_info = {}
            user_info['chat_id'] = data['message']['chat']['id']
            user_info['first_name'] = data['message']['chat']['first_name']
            user_info['user_request'] = data['message']['text']
            send_response(user_info=user_info)
        return HttpResponse('<h2>POST Request Greetings from India !!!!!!!!</h2>')

def send_response(user_info):
    if str(user_info['user_request']).lower() == 'hello sayani':
        url = "https://api.telegram.org/bot" + SAYONAARA_API_KEY + '/sendMessage?chat_id=' + user_info['chat_id']
        text_response = 'Hello ' + user_info['first_name'] + '\n' + 'Let me know where would you like to spend your vacation ?  '
        payload = {
            "text": text_response,
            "disable_web_page_preview": False,
            "disable_notification": False,
            "reply_to_message_id": None
        }
        headers = {
            "Accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "Content-Type": "application/json"
        }
        esponse = requests.post(url, json=payload, headers=headers)
