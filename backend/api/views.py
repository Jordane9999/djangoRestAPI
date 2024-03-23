import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def api_view(request, *args, **kwargs):
    # request => HttpRequest
    print(request.body)  # ceci envoie un byte string (b'')
    # permet de convertir les donner en dictionnaire python plus precisement il enleve le byte string
    data = json.loads(request.body)
    print(data)
    # permet de renvoyer les donner sur la forme initial
    pre_data = json.dumps(data)
    print(pre_data)
    # ----------------------------
    # "dict" permet de convertir les donners de la requet au format dictionnaire python
    print("dic : ", dict(request.headers))
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post-data'] = dict(request.POST)
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
