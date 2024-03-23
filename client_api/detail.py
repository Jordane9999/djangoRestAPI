import requests
endpoint = "http://127.0.0.1:8000/product/2/detail"
response = requests.get(endpoint)
# Ceci permet de convertir les donner renvoyer au format json
print(response.json())
# Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
print(response.status_code)
