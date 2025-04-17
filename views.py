from django.shortcuts import render
import datetime
import json
import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_country_from_ip(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if data.get('status') == 'success':
            return data.get('country')
        else:
            return 'desconocido'
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la ubicación: {e}")
        return 'desconocido'

def increment_visit_count():
    try:
        with open('visitas.txt', 'r+') as f:
            count = int(f.read())
            count += 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
            return count
    except FileNotFoundError:
        with open('visitas.txt', 'w') as f:
            f.write('1')
            return 1
    except ValueError:
        with open('visitas.txt', 'w') as f:
            f.write('1')
            return 1

def hola_mundo(request):
    now = datetime.datetime.now()
    hora = now.hour
    ip_address = get_client_ip(request)
    pais = get_country_from_ip(ip_address)
    visitas = increment_visit_count()

    saludo = ''
    if 5 <= hora < 12:
        saludo = 'Buenos días'
    elif 12 <= hora < 20:
        saludo = 'Buenas tardes'
    else:
        saludo = 'Buenas noches'

    context = {
        'hora': hora,
        'saludo': saludo,
        'pais': pais,
        'visitas': visitas,
    }
    return render(request, 'hola.php', context)
