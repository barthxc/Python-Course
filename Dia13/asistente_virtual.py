import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#OPCIONES DE VOZ / IDIOMA - no funciona por ahora
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TT_MS_ES-ES-HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TT_MS_EN-US_ZIRA_11.0'

#escucha nuestro microfono y devuelve el audio como texto
def transformar_audio_en_texto():
    #almacenamos recognizer en variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:
        #tiempo de espera desde que se activa el microfono
        r.pause_threshold = 0.8

        #informar que comenzó la grabación
        print("Ya puedes hablar")

        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio,  language='es-es')

            #prueba de que pudo ingresar y transformar
            print("Dijiste:" + pedido)

            #devolver a pedido
            return pedido
        #En caso de que no comprenda el audio
        except sr.UnknownValueError:
            #prueba de que no comprendió el audio
            print("Ups no hay servicio")

            #devolver error
            return "sigo esperando"

        #en caso de no poder resolver el pedido
        except sr.RequestError:
            #prueba de que no comprendió el audio
            print("Ups, no entendí")
            #devolver error
            return "sigo esperando"

        #error inesperado
        except:
            #prueba de que no comprendió el audio
            print("Ups esto se ha roto")
            #devolver error
            return "espero"



#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)

    #pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()



#funcion para pedir el dia
def pedir_dia():
    #crear variables con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear una variable para el día de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con los nombre de los días
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sábado',
                  6:'Domingo'}
    #decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')



#informar de que hora es
def pedir_hora():
    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} y {hora.minute}'
    print(hora)

    #decir la hora
    hablar(hora)


#funcion saludo inicial

def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour <13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'
    #decir el saludo
    hablar(f'{momento}, soy Botilla. Porfavor, dime en que te puedo ayudar')


#funcion central del asistente
def pedir_cosas():
    #saludo inicial
    saludo_inicial()
    #variable de corte
    comenzar = True
    #loop central
    while comenzar:

        #activar el microfono y guardar el pedido en un string
        pedido= transformar_audio_en_texto().lower()
        if 'abre youtube' in pedido:
            hablar('Vale!, abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir el navegador' in pedido or 'abre el navegador' in pedido:
            hablar('Marchando una de navegador')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'a qué estamos' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'gracias' in pedido:
            hablar('De nada, estoy programada para chuparte el culo.')
            continue
        elif "busca en wikipedia" in pedido:
            hablar("buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente: ")
            hablar(resultado)
            continue
        elif 'me oyes' in pedido:
            hablar('te oigo perfectamente')
        elif 'busca en internet' in pedido:
            hablar('Voy creador mio')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('He encontrado esto')
            continue
        elif 'reproducir' in pedido or 'reproduce' in pedido:
            hablar('Mientras no sea porno, todo bien')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'Aquí la tienes socio, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Lo siento compi, no encontré una mierda')
                continue
        elif 'adiós' in pedido:
            hablar('Venga me cierro que me cansas, humano de pacotilla')
            break
pedir_cosas()