import random
from manejo_de_imagenes import *
DIMENSION_PANTALLA = (800, 600)
pantalla = pygame.display.set_mode(DIMENSION_PANTALLA)
RUTA_FONDO = "superficies/5p7l34835j8c1.jpeg"
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (255, 0, 0)
COLOR_VIOLETA = (255, 0, 255)
COLOR_BLANCO = (255, 255, 255)

lista_preguntas = {"Preferirias tener un auto o una moto": ["Tener un auto", "Tener una moto"], "Ser inmortal o ser millonario": ["Ser inmortal", "Ser millonario"]
                   , "Que fue primero el huevo o la gallina": ["El huevo", "La gallina"], "Codear en Python o en Java": ["En Python", "En Java"]}

