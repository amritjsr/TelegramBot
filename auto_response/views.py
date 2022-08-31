from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def hello_world(request):
    if str(request.method).upper() == 'GET':
        return HttpResponse('<h2>GET Request .... Greetings from India !!!!!!!!</h2>')
    elif str(request.method).upper() == 'POST':
        # print(request.POST)
        print(request.body.decode('UTF-8'))
        return HttpResponse('<h2>POST Request Greetings from India !!!!!!!!</h2>')
    


# (vPy310Env) amritendudas@amritendudas-mac ~ % ptpython
# >>> import json
# >>> {"update_id":2727769,
# ... "message":{"message_id":1564,"from":{"id":854926804,"is_bot":false,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","language_code":"e
# ... n"},"chat":{"id":854926804,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","type":"private"},"date":1661619923,"text":"Amrit Here"}}
# >>> data = """{"update_id":2727769,
# ... "message":{"message_id":1564,"from":{"id":854926804,"is_bot":false,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","language_code":"e
# ... n"},"chat":{"id":854926804,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","type":"private"},"date":1661619923,"text":"Amrit Here"}}"
# ... ""
# >>> msg_in_json = json.loads(data)
# >>> msg_in_json.keys()
# dict_keys(['update_id', 'message'])

# >>> msg_in_json['message']
# {'message_id': 1564, 'from': {'id': 854926804, 'is_bot': False, 'first_name': 'Amritendu', 'last_name': 'Das', 'username': 'amritjsr', 'language_code': 'en'}, 'chat': {'id': 854926804, 'first_name': 'Amritendu', 'last_name': 'Das', 'username': 'amritjsr', 'type': 'private'}, 'date': 1661619923, 'text': 'Amrit Here'}

# >>> msg_in_json['message'].keys()
# dict_keys(['message_id', 'from', 'chat', 'date', 'text'])

# >>> msg_in_json['message']['from']
# {'id': 854926804, 'is_bot': False, 'first_name': 'Amritendu', 'last_name': 'Das', 'username': 'amritjsr', 'language_code': 'en'}

# >>> msg_in_json['message']['from']['first_name']
# 'Amritendu'

# >>> msg_in_json['message']['from']['last_name']
# 'Das'

# >>> msg_in_json['message']['chat']
# {'id': 854926804, 'first_name': 'Amritendu', 'last_name': 'Das', 'username': 'amritjsr', 'type': 'private'}

# >>> msg_in_json['message']['chat']['id']
# 854926804

# >>> msg_in_json['message']['chat']['id']
# 854926804

# >>> data02 = """{"update_id":2727770,
# ... "message":{"message_id":1565,"from":{"id":854926804,"is_bot":false,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","language_code":"e
# ... n"},"chat":{"id":854926804,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","type":"private"},"date":1661620622,"photo":[{"file_id":"A
# ... gACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgADcwADKQQ","file_unique_id":"AQADU7ExG2XsWVR4","file_size":564,"width":90,"he
# ... ight":40},{"file_id":"AgACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgADbQADKQQ","file_unique_id":"AQADU7ExG2XsWVRy","file_s
# ... ize":7569,"width":320,"height":144},{"file_id":"AgACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgADeAADKQQ","file_unique_id":
# ... "AQADU7ExG2XsWVR9","file_size":30645,"width":800,"height":361},{"file_id":"AgACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgA
# ... DeQADKQQ","file_unique_id":"AQADU7ExG2XsWVR-","file_size":41754,"width":1238,"height":558}]}}"""
# >>> msg_in_json02 = json.loads(data02)
# >>> msg_in_json02['message'].keys()
# dict_keys(['message_id', 'from', 'chat', 'date', 'photo'])

# >>> msg_in_json['message'].keys()
# dict_keys(['message_id', 'from', 'chat', 'date', 'text'])

# >>> msg_in_json02['message']['data']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'data'

# 'data'
# >>> msg_in_json02['message']['date']
# 1661620622

# >>> msg_in_json02['message']['photo']
# [{'file_id': 'AgACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgADcwADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVR4', 'file_size': 564, 'width': 90, 'height': 40}, {'file_id': 'AgACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgADbQADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVRy', 'file_size': 7569, 'width': 320, 'height': 144}, {'file_id': 'AgACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgADeAADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVR9', 'file_size': 30645, 'width': 800, 'height': 361}, {'file_id': 'AgACAgUAAxkBAAIGHWMKUY6X26clWPcJTTzMwcmSHVR9AAJTsTEbZexZVBPaFB3LQPZ3AQADAgADeQADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVR-', 'file_size': 41754, 'width': 1238, 'height': 558}]

# >>> msg_in_json03 = json.loads("""{"update_id":2727771,
# ... "message":{"message_id":1566,"from":{"id":854926804,"is_bot":false,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","language_code":"e
# ... n"},"chat":{"id":854926804,"first_name":"Amritendu","last_name":"Das","username":"amritjsr","type":"private"},"date":1661620800,"photo":[{"file_id":"A
# ... gACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgADcwADKQQ","file_unique_id":"AQADU7ExG2XsWVR4","file_size":564,"width":90,"he
# ... ight":40},{"file_id":"AgACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgADbQADKQQ","file_unique_id":"AQADU7ExG2XsWVRy","file_s
# ... ize":7569,"width":320,"height":144},{"file_id":"AgACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgADeAADKQQ","file_unique_id":
# ... "AQADU7ExG2XsWVR9","file_size":30645,"width":800,"height":361},{"file_id":"AgACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgA
# ... DeQADKQQ","file_unique_id":"AQADU7ExG2XsWVR-","file_size":41754,"width":1238,"height":558}],"caption":"aha pics"}}""")
# >>> msg_in_json03['message']
# {'message_id': 1566, 'from': {'id': 854926804, 'is_bot': False, 'first_name': 'Amritendu', 'last_name': 'Das', 'username': 'amritjsr', 'language_code': 'en'}, 'chat': {'id': 854926804, 'first_name': 'Amritendu', 'last_name': 'Das', 'username': 'amritjsr', 'type': 'private'}, 'date': 1661620800, 'photo': [{'file_id': 'AgACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgADcwADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVR4', 'file_size': 564, 'width': 90, 'height': 40}, {'file_id': 'AgACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgADbQADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVRy', 'file_size': 7569, 'width': 320, 'height': 144}, {'file_id': 'AgACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgADeAADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVR9', 'file_size': 30645, 'width': 800, 'height': 361}, {'file_id': 'AgACAgUAAxkBAAIGHmMKUkBqkIeR6enEYKKAguNAW8doAAJTsTEbZexZVBPaFB3LQPZ3AQADAgADeQADKQQ', 'file_unique_id': 'AQADU7ExG2XsWVR-', 'file_size': 41754, 'width': 1238, 'height': 558}], 'caption': 'aha pics'}

# >>> msg_in_json03['message'].keys()
# dict_keys(['message_id', 'from', 'chat', 'date', 'photo', 'caption'])
