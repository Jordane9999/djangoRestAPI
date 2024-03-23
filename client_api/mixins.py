import requests

# ======Creations d'un produit======

# endpoint = "http://127.0.0.1:8000/product/mixins/create/"
# response = requests.post(endpoint, json={
#                          "name": "Roger", "content": "C'est juste roger ", "price": 300})
# # Ceci permet de convertir les donner renvoyer au format json
# print(response.json())
# # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
# print(response.status_code)


# ======Mise ajour d'un produit======

# endpoint = "http://127.0.0.1:8000/product/mixins/update/8/"
# """
# NB: pour faire une modification totale sur les donner on utilise un "put" et pour faire une modification partielle sur les elements on fait un "patch"
# """
# response = requests.patch(
#     endpoint, json={'content': 'Je suis la mangue'})
# # Ceci permet de convertir les donner renvoyer au format json
# print(response.json())
# # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
# print(response.status_code)


# ======Liste des produit======

# endpoint = "http://127.0.0.1:8000/product/mixins/list/"
# response = requests.get(endpoint)
# # Ceci permet de convertir les donner renvoyer au format json
# print(response.json())
# # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
# print(response.status_code)


# ======Supprimer un produit======

# id = input("enter the id of product that you want to delet : ")
# endpoint = f"http://127.0.0.1:8000/product/mixins/delete/{id}/"
# """
# NB: pour faire une modification totale sur les donner on utilise un "put" et pour faire une modification partielle sur les elements on fait un "patch"
# """
# response = requests.delete(endpoint)
# # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
# print(response.status_code, response.status_code == 204)


# ======le detail d'un produit======

endpoint = "http://127.0.0.1:8000/product/mixins/3/"
response = requests.get(endpoint)
# Ceci permet de convertir les donner renvoyer au format json
print(response.json())
# Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
print(response.status_code)


"""
Nb : chacune de ces clients doit etre mis dans des fichier different comme cela as ete faite avec des class different de la vue donc sacher que ce qui est fait ici est un test de verrification
"""
