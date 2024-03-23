import requests
endpoint = "http://127.0.0.1:8000/product/create/"
response = requests.post(endpoint, json={
                         "name": "ma nouvelle formation", "content": " ", "price": 200})
# Ceci permet de convertir les donner renvoyer au format json
print(response.json())
# Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
print(response.status_code)
