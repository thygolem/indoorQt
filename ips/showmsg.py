import time

actives = {'alias': ['iván'],
            'mac' : ['00:00:00:00:00:01'],
            'zone': ['']}


zones = {'B/F/Z': ['A/A/A'],
        'mac'   : ['BF:Z0:00:00:00:01'],
        'rssi'  : [-56]}

zonesB = {'A': {'x' : 1, 'y': 1, 'z' : 1}}, {'B': {'x' : 2, 'y' : 2, 'z' : 2}}

def show_data(topic = 'indoor', esp32 = '', userMac = '0', rssi = 0):
    listening = True
    print('Connecting to Broker w/ Topic: {}'.format(topic))
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    distance = rssi * 0.5
    while listening == True:
        if userMac == '10:00:00:00:00:01':
            if esp32 == 'BF:Z0:00:00:00:01':
                position = actives['zone'][0] = 'A'
                return actives
            elif esp32 == 'BF:Z0:00:00:00:02':
                position = actives['zone'][0] = 'B'
                return actives
    else:
        return 'Conectar con broker'



show_topic = show_data(topic = 'indoor', esp32 = 'BF:Z0:00:00:00:02', userMac = '10:00:00:00:00:01', rssi = -56)

print(show_topic)

# cap 134 funciones


'''
MEJORAS:
    En caso de no hacer triangulación:

    - Las antenas pueden estar encontrándose entre ellas y de esta manera podemos 
    configurar el nivel al que actúa el threshold.
    
    - Se trata de nos crear 'positivos' en varias zonas de manera simultánea.

        - Si aumentamos el valor de threshold (RSSI) +=1 cada vez que un esp32 detecta a esp32',
        la configuración del threshold puede quedar ajustada de manera automática.
        
        -El punto es dejar de añadir valores al threshold cuando esp32 ya no detecte más esp32'

'''