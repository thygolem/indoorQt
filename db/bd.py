import psycopg2
import json
# Leer las credenciales de un archivo JSON
# Recomendado: https://parzibyte.me/blog/2019/06/09/json-python-codificar-decodificar/
with open("credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)
# Como la conexión devuelve un diccionario podemos convertirlo fácilmente
# a "kwargs" o key arguments ;)
# Recomendado: https://parzibyte.me/blog/2018/12/20/args-kwargs-python/
try:
    conn = psycopg2.connect(**credenciales)
    print('yes')
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)