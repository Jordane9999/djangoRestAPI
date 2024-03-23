import requests
endpoint = "http://127.0.0.1:8000/product/update/1/"
"""
NB: pour faire une modification totale sur les donner on utilise un "put" et pour faire une modification partielle sur les elements on fait un "patch"
"""
response = requests.patch(
    endpoint, json={'content': ' '})
# Ceci permet de convertir les donner renvoyer au format json
print(response.json())
# Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
print(response.status_code)
