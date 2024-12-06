import json
import pygame
from manejo_de_imagenes import *
from variables import *

def leer_json(path):
    with open(path, 'r') as file:
        lectura = json.load(file)
        return lectura
    
def cuenta_regresiva(tiempo_limite):    
    evento_ticks_1 = pygame.USEREVENT + 1 
    tiempo_miliseg = 1000
    tiempo_limite -= 1
    pygame.time.set_timer(evento_ticks_1, tiempo_miliseg)
    if tiempo_limite == 0:
        pygame.quit()
        quit()

def porcentaje_votos(lista, azules, rojas):
    porcentaje_azul = (len(lista) - azules) / 100
    porcentaje_rojo = (len(lista) - rojas) / 100
    cuadro_porcentaje = CrearCuadro(pantalla, COLOR_VERDE, (250, 300, 400, 40))
