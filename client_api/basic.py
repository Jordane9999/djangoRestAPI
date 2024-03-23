import requests


endpoint = "http://127.0.0.1:8000/api/"
response = requests.get(endpoint, json={})
# Ceci permet de convertir les donner renvoyer au format json
print(response.json())
# Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
print(response.status_code)


endpoint = "http://127.0.0.1:8000/product/"
response = requests.post(
    endpoint, json={"name": "Pasteqe", "content": "Description here", "price": 20.32})
# Ceci permet de convertir les donner renvoyer au format json
print(response.json())
# Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
print(response.status_code)

# HTTP REQUEST --> HTML
# REST API HTTP --> JSON


""" 
    - Si les donner sont envoyer depuis le backend sous form de dictionnaire claire 
    il n'y a plus besoin d'ajouter le second parametre dans 
        # requests.get(endpoint) et le response.json() va bien prendre  
        les donner de format
        exemple 1:
            ## Fichier view.py
            def api_view(request, *args, **kwargs):
                data = {
                    "kodjo": "kokou"
                }
                return JsonResponse(data)

            ## Fichier basic.py (client)
            endpoint = "url_precis vers cette view"
            response = requests.get(endpoint)
            # Ceci permet de convertir les donner renvoyer au format json
            print(response.json())
            # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
            print(response.status_code)

    - Dans le cas contraire il faut ajouter un second parametre dans le
        # requests.get(endpoint) et le response.json() va bien prendre 

        exemple 2:
            ## Fichier view.py
            def api_view(request, *args, **kwargs):
                # request => HttpRequest
                print(request.body)  # ceci envoie un byte string (b'')
                # permet de convertir les donner en diction,aire python
                data = json.loads(request.body)
                print(data)
                # permet de renvoyer les donner sur la forme initial
                pre_data = json.dumps(data)
                print(pre_data)
                # ----------------------------
                data['headers'] = dict(request.headers)
                data['params'] = dict(request.GET)
                data['post-data'] = dict(request.POST)
                print(request.headers)
                data['content_type'] = request.content_type
                
                return JsonResponse(data)            
            
            ## Fichier basic.py (client)
            endpoint = "url_precis vers cette view"
            response = requests.get(endpoint, json={}) # Vous pouvez ajouter aussi des donner au json
            # Ceci permet de convertir les donner renvoyer au format json
            print(response.json())
            # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
            print(response.status_code)

"""
