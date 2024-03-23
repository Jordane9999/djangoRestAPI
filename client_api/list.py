import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/product/auth/"
username = input('Entrer votre username : ')
password = getpass('Entrer votre password : ')
auth_response = requests.post(
    endpoint, json={"username": username, "password": password})
print(auth_response.json())
print(auth_response.status_code)
print(type(auth_response.status_code))

# utilisation du token pour  connecter le client
if auth_response.status_code == 200:
    endpoint = "http://127.0.0.1:8000/product/list/"
    headers = {
        # 'Authorization': 'Token 87b8ed729d19f861c43c72d4da57a3ac9712e42f' # Ceci c'est l'authentification par defaut
        # Ceci c'est une authentification perssonnaliser avec un temp d'espiration
        'Authorization': 'Bearer 87b8ed729d19f861c43c72d4da57a3ac9712e42f'
    }
    response = requests.get(endpoint, headers=headers)
    # Ceci permet de renvoyer les donner au format json
    print(response.json())
    # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
    print(response.status_code)


# == la seconde methode de listage

# endpoint = "http://127.0.0.1:8000/product/list2/"
# response = requests.get(endpoint)
# # Ceci permet de convertir les donner renvoyer au format json
# print(response.json())
# # Ceci permet de renvoyer l'etat de l'envoie(200, 405, 300, ...)
# print(response.status_code)
