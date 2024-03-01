import dateparser
from fuzzywuzzy import process
from unidecode import unidecode
import re
from pathlib import Path

def identificar_formato_fecha(date: str, dateFormat: str = "%Y-%m-%d", lang: str = 'en'):
    try:
        settings = {'STRICT_PARSING': True}
        parsed_date = dateparser.parse(date, settings=settings, languages=[lang])
        return parsed_date.strftime(dateFormat)
    except (ValueError, AttributeError):
        return None


# Función que pasando un texto transforma las fechas de mes y año en número
def texto_a_numero(texto: str, tipo: str = 'Dia'):
    dia = {'uno': '1', 'dos': '2', 'tres': '3', 'cuatro': '4', 'cinco': '5', 'seis': '6', 'siete': '7', 'ocho': '8',
           'nueve': '9', 'diez': '10', 'once': '11', 'doce': '12', 'trece': '13', 'catorce': '14', 'quince': '15',
           'dieciseis': '16', 'diecisiete': '17', 'dieciocho': '18', 'diecinueve': '19', 'veinte': '20',
           'veintiuno': '21', 'veintidos': '22', 'veintitres': '23', 'veinticuatro': '24', 'veinticinco': '25',
           'veintiseis': '26', 'veintisiete': '27', 'veintiocho': '28', 'veintinueve': '29', 'treinta': '30',
           'treinta y uno': '31', 'mil': '1000', 'dos mil': '2000',
           'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9',
           'X': '10', 'XI': '11', 'XII': '12', 'XIII': '13', 'XIV': '14', 'XV': '15', 'XVI': '16', 'XVII': '17',
           'XVIII': '18', 'XIX': '19', 'XX': '20', 'XXI': '21', 'XXII': '22', 'XXIII': '23', 'XXIV': '24', 'XXV': '25',
           'XXVI': '26', 'XXVII': '27', 'XXVIII': '28', 'XXIX': '29', 'XXX': '30', 'XXXI': '31'}

    mes = {'enero': '1', 'febrero': '2', 'marzo': '3', 'abril': '4', 'mayo': '5', 'junio': '6', 'julio': '7',
           'agosto': '8', 'septiembre': '9', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'}

    anio = {'mil novecientos noventa': 1990, 'mil novecientos noventa y uno': 1991,
            'mil novecientos noventa y dos': 1992,
            'mil novecientos noventa y tres': 1993, 'mil novecientos noventa y cuatro': 1994,
            'mil novecientos noventa y cinco': 1995, 'mil novecientos noventa y seis': 1996,
            'mil novecientos noventa y siete': 1997, 'mil novecientos noventa y ocho': 1998,
            'mil novecientos noventa y nueve': 1999, 'dos mil': 2000, 'dos mil uno': 2001,
            'dos mil dos': 2002, 'dos mil tres': 2003, 'dos mil cuatro': 2004, 'dos mil cinco': 2005,
            'dos mil seis': 2006, 'dos mil siete': 2007, 'dos mil ocho': 2008,
            'dos mil nueve': 2009, 'dos mil diez': 2010, 'dos mil once': 2011, 'dos mil doce': 2012,
            'dos mil trece': 2013, 'dos mil catorce': 2014, 'dos mil quince': 2015,
            'dos mil dieciseis': 2016, 'dos mil diecisiete': 2017, 'dos mil dieciocho': 2018,
            'dos mil diecinueve': 2019, 'dos mil veinte': 2020, 'dos mil veintiuno': 2021,
            'dos mil veintidos': 2022, 'dos mil veintitres': 2023, 'dos mil veinticuatro': 2024,
            'dos mil veinticinco': 2025}

    texto = texto.replace(' y ', '')
    if 'Dia' in tipo:
        numero = dia
    elif 'Mes' in tipo:
        numero = mes
    else:
        numero = anio

    match = process.extractOne(texto, numero.keys())

    # Comprobamos el porcentaje de similitud y lo ponemos en un 80%
    if match[1] > 70:
        return numero[match[0]]

    return texto


def dia_a_numero(texto: str):
    return texto_a_numero(texto, tipo='Dia')


def mes_a_numero(texto: str):
    return texto_a_numero(texto, tipo='Mes')


def anio_a_numero(texto: str):
    return texto_a_numero(texto, tipo='Anio')

# Limpiar fecha
def limpiar_fecha(fecha):
    dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    # Convertir los días de la semana a minúsculas y sin tildes
    dias_semana_lower = [unidecode(dia.lower()) for dia in dias_semana]

    # Crear una expresión regular para buscar cualquier día de la semana
    regex_dias = '|'.join(dias_semana_lower)
    fecha = re.sub(regex_dias, '', fecha, flags=re.IGNORECASE).strip()

    # Eliminar palabras innecesarias y caracteres especiales
    # return fecha.replace('a ', '').replace('del', '').replace('de', '').replace('año', '').replace('.', '').replace('/', '').replace('-', '')
    fecha = re.sub('a ', '', fecha, flags=re.IGNORECASE).strip()
    fecha = re.sub('del', '', fecha, flags=re.IGNORECASE).strip()
    fecha = re.sub('de', '', fecha, flags=re.IGNORECASE).strip()
    fecha = re.sub('dia', '', fecha, flags=re.IGNORECASE).strip()
    fecha = re.sub('día', '', fecha, flags=re.IGNORECASE).strip()
    fecha = re.sub('mes', '', fecha, flags=re.IGNORECASE).strip()
    fecha = re.sub('año', '', fecha, flags=re.IGNORECASE).strip()
    return fecha.replace(':', '').replace('.', '').replace('/', '').replace('-', '')


# Función que pasada una fecha en texto devuelve una lista con el dia, mes y año
def formatear_fecha(fecha: str):
    fecha_formateada = limpiar_fecha(fecha)

    # Dividir la cadena formateada en una lista
    lista_fecha = fecha_formateada.split()

    # Unir cuando hay un 'y'
    for i in range(1, len(lista_fecha)):
        if lista_fecha[i] == 'y':
            lista_fecha[i - 1:i + 2] = [' '.join(lista_fecha[i - 1:i + 2])]
            break
    # Unir cuando hay un segundo 'y'
    for i in range(1, len(lista_fecha)):
        if lista_fecha[i] == 'y':
            lista_fecha[i - 1:i + 2] = [' '.join(lista_fecha[i - 1:i + 2])]
            break

    # Unir 'dos', 'mil', 'dieciseis' en 'dos mil dieciseis'
    if len(lista_fecha) > 3:
        lista_fecha[2:6] = [' '.join(lista_fecha[2:6])]

    return lista_fecha


# Función que transforma fechas YYYY.MM.DD y DD.MM.YYYY en YYYY-MM-DD
def formatear_fecha_simbolo(fecha: str):
    # Verificar si la fecha está en formato "YYYY.MM.DD"
    if re.match(r'\d{4}\.\d{2}\.\d{2}', fecha):
        partes = fecha.split('.')
        fecha_formateada = partes[0] + '-' + partes[1] + '-' + partes[2]
    # Verificar si la fecha está en formato "DD.MM.YYYY"
    elif re.match(r'\d{2}\.\d{2}\.\d{4}', fecha):
        partes = fecha.split('.')
        fecha_formateada = partes[2] + '-' + partes[1] + '-' + partes[0]
    else:
        fecha_formateada = None

    return fecha_formateada


def transform_date(fecha: str, dateFormat: str = "%Y-%m-%d"):
    proceso = "dateparser"
    formato_identificado = identificar_formato_fecha(fecha)
    if formato_identificado is None:
    
        try:
            # Formato AAAA.MM.DD
            proceso = "AAAA.MM.DD"
            formato_identificado = formatear_fecha_simbolo(fecha)

            if formato_identificado is None:
                proceso = "fuzzywuzzy"

                fecha_formateada = formatear_fecha(fecha)

                fecha_formateada[0] = str(dia_a_numero(fecha_formateada[0]))
                fecha_formateada[1] = str(mes_a_numero(fecha_formateada[1]))
                fecha_formateada[2] = str(anio_a_numero(fecha_formateada[2]))

                # Convertir la lista a una cadena separada por espacios
                cadena_formateada = ' '.join(fecha_formateada)

                formato_identificado = identificar_formato_fecha(cadena_formateada)
        except:
            print(fecha)
    return {
        "proceso": proceso,
        "fecha": fecha,
        "formato_identificado": formato_identificado
    }


def get_dates_from_file():
    file_path = '/app/app/ProFechEtiq.txt'
    file_path_obj = Path(file_path)
    
    if not file_path_obj.is_file():
        return {"error": "El archivo no existe."}
    dates = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            dates.append(line.strip())
    return dates