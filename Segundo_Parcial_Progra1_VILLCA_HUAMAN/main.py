import pygame
from widgets import Button
from variables import *
from manejo_de_imagenes import *
import random

def elegir_respuesta(pregunta):
    contador_respuesta_azul = 0
    contador_respuesta_roja = 0
    #pregunta_aleatoria = random.choice(list(lista_preguntas.keys()))
    for i in range(0, 4):
        respuesta_aleatoria = random.choice(list(lista_preguntas[pregunta]))
        if respuesta_aleatoria == lista_preguntas[pregunta][0]:
            contador_respuesta_azul += 1
        elif respuesta_aleatoria == lista_preguntas[pregunta][1]:
            contador_respuesta_roja += 1
    if contador_respuesta_azul > contador_respuesta_roja:
        return cuadro_azul.coordenada
    else:
        return cuadro_rojo.coordenada

pygame.init()

bandera = True
CrearImagen(RUTA_FONDO, pantalla, DIMENSION_PANTALLA)
boton = Button(350, 250, "HOLAS JOROLAS", pantalla, 40)
boton.update()
boton.draw()
cuadro_pregunta = CrearCuadro(pantalla, COLOR_BLANCO, (250, 450, 350, 40))
rect_pregunta = cuadro_pregunta.coordenada
cuadro_azul = CrearCuadro(pantalla, COLOR_AZUL, (250, 500, 170, 40))
cuadro_rojo = CrearCuadro(pantalla, COLOR_ROJO, (430, 500, 170,40))
comodines = [CrearCuadro(pantalla, COLOR_VERDE, (560, 400, 40, 40)),
            CrearCuadro(pantalla, COLOR_VERDE, (510, 400, 40, 40)),
            CrearCuadro(pantalla, COLOR_VERDE, (460, 400, 40, 40))]
puntaje = CrearTexto("arial", 24, "PUNTAJE: ", COLOR_VIOLETA, pantalla, (630, 60))


while True:
    pygame.display.flip()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            pregunta_aleatoria = random.choice(list(lista_preguntas.keys()))
            if elegir_respuesta(pregunta_aleatoria).collidepoint(mouse_pos):
                cuadro_pregunta = CrearCuadro(pantalla, COLOR_BLANCO, (250, 450, 350, 40))
                cuadro_azul = CrearCuadro(pantalla, COLOR_AZUL, (250, 500, 170, 40))
                cuadro_rojo = CrearCuadro(pantalla, COLOR_ROJO, (430, 500, 170,40))
                texto_pregunta = CrearTexto("arial", 30, pregunta_aleatoria, COLOR_VERDE, pantalla, (260, 455))
                texto_respuesta_1 = CrearTexto("comic sans", 30, lista_preguntas[pregunta_aleatoria][0], COLOR_VERDE, pantalla, (260, 495))
                texto_respuesta_2 = CrearTexto("comic sans", 30, lista_preguntas[pregunta_aleatoria][1], COLOR_VERDE, pantalla, (440, 495))
                bandera = False
                lista_preguntas.pop(pregunta_aleatoria)
    pygame.display.update()