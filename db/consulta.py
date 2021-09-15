import psycopg2
from bd import conn

#def update_zone_occupation(zone_id, zone_people_inside):
'''Actualizar los person_mac que se encuentran en la zona'''


try:
    with conn.cursor() as cur:
        # En este caso no necesitamos limpiar ningún dato
        cur.execute("SELECT id, zone_name, zone_people_inside FROM bfz_zone;")
        # print('Hay {} personas en la zona'.format(zone_people_inside))

        # Con fetchall traemos todas las filas
        bfz_data = cur.fetchall()

        # Recorrer e imprimir
        for bfz in bfz_data:
            print(bfz)
        
        esp32_status = 1

        update_position = "UPDATE bfz_zone SET zone_people_inside = 7 WHERE id = 1;"
        #zone_people_inside = 1
        #cur.execute(update_position, (zone_people_inside))
        cur.execute(update_position)
        conn.commit()
        count = cur.rowcount
        print(count)


        
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conn.close()