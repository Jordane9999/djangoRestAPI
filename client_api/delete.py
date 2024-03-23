import requests

id = input("enter the id of product that you want to delet : ")
endpoint = f"http://127.0.0.1:8000/product/delete/{id}/"
"""
NB: pour faire une modification totale sur les donner on utilise un "put" et pour faire une modification partielle sur les elements on fait un "patch"
"""
response = requests.delete(endpoint)
# Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
print(response.status_code, response.status_code == 204)
