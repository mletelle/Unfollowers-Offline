import json   # Importo la librería que me permite leer archivos .json, el formato que usa Instagram.
import os     # Esta me sirve para manejar rutas de archivos sin depender del sistema operativo.

'''Esta función se encarga de abrir uno de los archivos (followers o following)
    y sacar de ahí los nombres de usuario. Es lo único que hace.'''
def load_usernames(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:  # Abre el archivo que le paso por parametro
        data = json.load(file)  # Lo carga en memoria como estructura de Python (puede ser dict o list)

    usernames = set()  # Acá voy a guardar los nombres de usuario, sin repetirlos

    # Si el json arranca como diccionario (clave/valor), probablemente sea el formato de 'following.json'
    if isinstance(data, dict):
        for key in ['relationships_following', 'relationships_followers']:  # Busco estas dos claves porlas dudas
            if key in data: # Si la clave está, me quedo con el valor que tiene 
                data = data[key]  # Me quedo con la lista que está dentro de esa clave

    # Si lo que tengo ahora es una lista (de diccionarios), sigo procesando
    if isinstance(data, list):
        for entry in data: # Recorro cada ítem de la lista (cada uno es un diccionario)
            # Me aseguro que cada ítem tenga la clave "string_list_data"
            if isinstance(entry, dict) and "string_list_data" in entry: 
                string_data = entry["string_list_data"]
                # Me fijo que sea una lista no vacía
                if isinstance(string_data, list) and len(string_data) > 0:
                    value = string_data[0].get("value")  # Acá está el nombre del usuario
                    if value: # Me aseguro que no sea None o vacío
                        usernames.add(value)  # Lo agrego al set (sin repes)

    return usernames  # Devuelvo el set con todos los nombres que encontré

# Esta es la función principal, la que se corre cuando arrancás el script
def main_console():
    # Detecta en qué carpeta está el archivo .py, para buscar ahí mismo los JSON
    downloads = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    # Asumo que en esa carpeta están los archivos JSON que descargaste de Instagram
    followers_file = os.path.join(downloads, 'followers_1.json')
    following_file = os.path.join(downloads, 'following.json')

    # Cargo los nombres desde cada archivo
    followers = load_usernames(followers_file)
    following = load_usernames(following_file)

    # Resto de conjuntos: acá saco los que sigo pero no me siguen
    not_following_back = following - followers
    # Y los que me siguen a mí pero yo no los sigo 
    not_followed_by_me = followers - following

    # Muestra en pantalla quién no me sigue de vuelta
    print("Usuarios a los que sigo y que NO me siguen de vuelta:")
    for user in sorted(not_following_back): # Ordeno alfabéticamente
        print("  -", user) # Muestra quién no me sigue de vuelta

    # Muestra quién me sigue y yo no sigo
    print("\nUsuarios que me siguen y que YO no sigo de vuelta:")
    for user in sorted(not_followed_by_me): # Ordeno alfabéticamente
        print("  -", user) # Muestra quién me sigue y yo no sigo

# Este if se asegura que el script se ejecute solo cuando lo corrés directamente (no si lo importás)
if __name__ == '__main__':
    main_console() # Llama a la función principal para que arranque el programa
