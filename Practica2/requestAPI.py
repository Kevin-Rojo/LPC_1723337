import requests

# pokemon = input("Ingresa el nombre o numero de pokedex del pokemon: ")
# url = "https://pokeapi.co/api/v2/pokemon/"+pokemon
# respuesta = requests.get(url)
# datos = respuesta.json()

# print("Nombre: " + datos['forms'][0]['name'])
# print("Habilidades:")
# for habilidad in datos['abilities']:
#     print(" -" + habilidad['ability']['name'])
# print("Tipo:")
# for tipos in datos['types']:
#     print(" -" + tipos['type']['name'])
# print("\n")

coin = input("Ingrese una cripto moneda: ")
apikey = "sjcti6fu8poo6c75rnf00f"
url2 = 'https://api.lunarcrush.com/v2?/data=assets&key=' + apikey + '&symbol=' + coin
print(url2)
respuesta2 = requests.get(url2)
datos2 = respuesta2.json()

print(datos2)