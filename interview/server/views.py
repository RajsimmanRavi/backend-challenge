from django.shortcuts import render
from django.http import HttpResponse
from server.models import Conversation
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from django.forms.models import model_to_dict
import json

# Create your views here.

# Accept only POST requests and don't worry about CSRF 
@csrf_exempt
@require_http_methods("POST")
def insert_messages(request):
    try: 
        data = json.loads(request.body)
        message = str(data["message"])
        sender = str(data["sender"])
        conversation_id = str(data["id"])
        created = datetime.now()
        if len(Conversation.objects.filter(conversation_id=conversation_id)) > 0:
            return JsonResponse({'type': 'error', 'message': 'An object with the same ID is already stored.. Please provide a unique ID'})
        else:
            Conversation.objects.create(conversation_id=conversation_id, created=created, sender=sender, message=message)
            data = {'type': 'ok', 'message': 'Successfully stored message!'}
            return JsonResponse(data)
    except Exception as e:
        data = {'type': 'error', 'message': str(e)}
        return JsonResponse(data)
    

# Since we are looking for only Integer values (specified in urls.py), we don't need to substantially test or sanitize the input 
# as Django provides that functionality
# Here we are only accepting GET requests
@require_http_methods(["GET"])
def get_message(request, id):
    def datetime_to_str_converter(o):
        if isinstance(o, datetime):
            return o.__str__()
    try:
        return_object = Conversation.objects.get(conversation_id=id)
        return_dict = model_to_dict(return_object) # for returning properly
        return_json_dict = json.dumps(return_dict, default = datetime_to_str_converter) # need to convert the timestamp to string
        data = {'type': 'ok', 'data': json.loads(return_json_dict)}
        return JsonResponse(data)
    except Exception as e:
        data = {'type': 'error', 'message': str(e)}
        return JsonResponse(data)

