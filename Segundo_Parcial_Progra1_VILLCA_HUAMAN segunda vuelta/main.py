import pygame
from variables import *
from manejo_de_imagenes import *
import random
from auxiliares import *

def elegir_respuesta(pregunta):
    contador_respuesta_azul = 0
    contador_respuesta_roja = 0
    for i in range(0, len(lista_preguntas)):
        respuesta_aleatoria = random.choice(list(lista_preguntas[pregunta]))
        if respuesta_aleatoria == lista_preguntas[pregunta][0]:
            contador_respuesta_azul += 1
        elif respuesta_aleatoria == lista_preguntas[pregunta][1]:
            contador_respuesta_roja += 1
    
    #porcentaje_votos(lista_preguntas, contador_respuesta_azul, contador_respuesta_roja)

    if contador_respuesta_azul > contador_respuesta_roja:
        print("cuadro azul")
        return cuadro_azul.coordenada
    else:
        print("cuadro rojo")
        return cuadro_rojo.coordenada

lista_preguntas = leer_json("archivo_preguntas.json")

pygame.init()

bandera = True
CrearImagen(RUTA_FONDO, pantalla, DIMENSION_PANTALLA)
cuadro_pregunta = CrearCuadro(pantalla, COLOR_BLANCO, (200, 450, 450, 40))
rect_pregunta = cuadro_pregunta.coordenada
cuadro_azul = CrearCuadro(pantalla, COLOR_AZUL, (200, 500, 200, 40))
cuadro_rojo = CrearCuadro(pantalla, COLOR_ROJO, (450, 500, 200,40))
comodines = [CrearCuadro(pantalla, COLOR_VERDE, (560, 400, 40, 40)),
            CrearCuadro(pantalla, COLOR_VERDE, (510, 400, 40, 40)),
            CrearCuadro(pantalla, COLOR_VERDE, (460, 400, 40, 40))]

puntaje = 0
incremento_puntaje = 0

evento_ticks_1 = pygame.USEREVENT + 1 
tiempo_miliseg = 1000
tiempo_limite = 15
pygame.time.set_timer(evento_ticks_1, tiempo_miliseg)

while True:
    pygame.display.flip()
    for evento in pygame.event.get():
        
        cuadro_puntaje = CrearCuadro(pantalla, COLOR_ROJO, (630, 60, 170,40))
        texto_puntaje = CrearTexto("arial", 24, "PUNTAJE: " + str(puntaje), COLOR_BLANCO, pantalla, (630, 60))
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == evento_ticks_1:
            tiempo_limite -= 1
            cuadro_tiempo = CrearCuadro(pantalla, COLOR_AZUL, (315, 100, 170, 40))
            texto_tiempo = CrearTexto("arial", 26, ("TIEMPO: " + str(tiempo_limite)), COLOR_BLANCO, pantalla, (320, 100))
            if tiempo_limite == 0:
                pygame.quit()
                quit()
        if len(lista_preguntas) == 0:
                print("Ganaste")
                pygame.quit()
                quit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            pregunta_aleatoria = random.choice(list(lista_preguntas.keys()))
            if (bandera == True) or (elegir_respuesta(pregunta_aleatoria).collidepoint(mouse_pos)):

                cuadro_pregunta = CrearCuadro(pantalla, COLOR_BLANCO, (200, 450, 450, 40))
                cuadro_azul = CrearCuadro(pantalla, COLOR_AZUL, (200, 500, 200, 40))
                cuadro_rojo = CrearCuadro(pantalla, COLOR_ROJO, (450, 500, 200,40))
                texto_pregunta = CrearTexto("arial", 30, pregunta_aleatoria, COLOR_VERDE, pantalla, (210, 455))
                texto_respuesta_1 = CrearTexto("comic sans", 30, lista_preguntas[pregunta_aleatoria][0], COLOR_VERDE, pantalla, (210, 495))
                texto_respuesta_2 = CrearTexto("comic sans", 30, lista_preguntas[pregunta_aleatoria][1], COLOR_VERDE, pantalla, (460, 495))

                puntaje += 10 + incremento_puntaje
                incremento_puntaje += 10

                tiempo_limite = 15

                bandera = False
                lista_preguntas.pop(pregunta_aleatoria)
    pygame.display.update()