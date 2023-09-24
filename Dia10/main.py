import pygame
import random
import math
from pygame import mixer
import io
import sys
import asyncio


'''PASAR LA FUENTE A OBJETO BYTE PARA LA EXPORTACION EN .EXE'''
def fuente_bytes(fuente):
    #Abre el archigo TTF en modo lectura binaria
    with open(fuente,'rb') as f:
        #Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
        #Crear un objeto BytesIO a partir de los bytes del archivo TTF
        return io.BytesIO(ttf_bytes)



#inicializo la pantalla Pygame
pygame.init()


#Creo la pantalla Tamaño de la pantalla
pantalla = pygame.display.set_mode((800,600))


#Titulo e Icono
pygame.display.set_caption("BartHxC Game")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')


#Agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)


#variables del JUGADOR
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 520
jugador_x_cambio = 0


#variables del ENEMIGO
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio= []
cantidad_enemigos = 8


#variables del DUPLICAR ENEMIGOS
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736)) #el maximo en el eje X
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)




#variables de LA BALA
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio= 2
bala_visible= False

#PUNTUACION
puntaje = 0
fuente_como_bytes = fuente_bytes('FreeSansBold.ttf')
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x= 10
texto_y= 10


#TEXTO FINAL DE JUEGO
final = pygame.font.Font(fuente_como_bytes,64)

def texto_final():
    mi_fuente_final = final.render('JUEGO TERMINADO',True , (255,255,255))
    pantalla.blit(mi_fuente_final, (60,200))


#funcion mostrar puntuacion
def mostrar_puntuacion(x,y):
    texto = fuente.render(f'Pts:{puntaje}', True,(255,255,255))
    pantalla.blit(texto,(x,y))


#FUNCION PARA EL JUGADOR, LA POSICION SE ESCRIBE EN UNA TUPLA
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

def enemigo(x,y,enemigo):
    pantalla.blit(img_enemigo[enemigo],(x,y))

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+16,y+10))

#DETECCION DE COLISION

def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_2-x_1,2) + math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    else:
        return False


#Loop del juego
se_ejecuta = True

    #Loop buscando el evento QUIT que es la X de la pantalla para cerrarse la ejecución del apantalla.
while se_ejecuta:
        pantalla.fill((0, 0, 0))  # Rellena la pantalla con color negro
        pantalla.blit(fondo, (0, 0))  # Dibuja el fondo al comienzo del bucle

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                se_ejecuta = False


    # Movimiento - KEYDOWN ES TECLA PRESIONADA
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_x_cambio= -0.5
                if evento.key == pygame.K_RIGHT:
                    jugador_x_cambio= 0.5
                if evento.key == pygame.K_SPACE:
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.set_volume(0.4)
                    sonido_bala.play()
                    if not bala_visible:
                        bala_x = jugador_x
                        disparar_bala(bala_x,bala_y)


    # KEYUP ES TECLA SOLTADA
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador_x_cambio= 0


    #MOFICICAR UBICACION DEL JUGADOR- MOVIMIENTO
        jugador_x +=jugador_x_cambio


    #MANTENER DENTRO DE LOS BORDES DE LA PANTALLA
        if jugador_x <= 0:
            jugador_x = 0
        elif jugador_x >= 736:
            jugador_x =  736


    # MOFICICAR UBICACION DEL ENEMIGO- MOVIMIENTO
        for e in range(cantidad_enemigos):
            #FIN DEL JUEGO
            if enemigo_y[e] > 500:
                for k in range(cantidad_enemigos):
                    enemigo_y[k] = 1000
                texto_final()
                break

            enemigo_x[e] += enemigo_x_cambio[e]


    # MANTENER DENTRO DE LOS BORDES DE LA PANTALLA AL ENEMIGO
            if enemigo_x[e] <= 0:
                enemigo_x_cambio[e] = 0.2
                enemigo_y[e] += enemigo_y_cambio[e]
            elif enemigo_x[e] >= 736:
                enemigo_x_cambio[e] = -0.2
                enemigo_y[e] += enemigo_y_cambio[e]


    # VERIFICACION DE COLISION
            colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.set_volume(0.3)
                sonido_colision.play()
                bala_visible = False
                bala_y = 500
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)  # el maximo en el eje X
                enemigo_y[e] = random.randint(50, 200)
            enemigo(enemigo_x[e] , enemigo_y[e],e) #CARGA DEL ENEMIGO


        #MOVIMIENTO BALA
        if bala_y <= -64:
            bala_y = 500
            bala_visible = False

        if bala_visible:
            disparar_bala(bala_x,bala_y)
            bala_y -= bala_y_cambio

        jugador(jugador_x,jugador_y)


    #MOSTRAR PUNTUACIÓN
        mostrar_puntuacion(texto_x,texto_y)


    #ACTUALIZAR
        pygame.display.update()


