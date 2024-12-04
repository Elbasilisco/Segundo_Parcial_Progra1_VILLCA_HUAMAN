import pygame

class CrearImagen():
    def __init__(self, ruta, superficie, coordenadas: tuple, coordenadas_aux = (0, 0)):
        imagen_raw = pygame.image.load(ruta)
        fondo = pygame.transform.scale(imagen_raw, (coordenadas))
        superficie.blit(fondo, coordenadas_aux)
        
        
class CrearTexto():
    def __init__(self, fuente: str, tamaño, mensaje, color, superficie, coordenadas: tuple, ruta = None):
        self.letra = pygame.font.SysFont(fuente, tamaño)
        self.imagen = self.letra.render(mensaje, True, color)
        superficie.blit(self.imagen, coordenadas)

class CrearCuadro():
    def __init__(self, superficie, color, coordenadas):
        self.coordenada = pygame.Rect(coordenadas)
        self.cuadro = pygame.draw.rect(superficie, color, pygame.Rect(coordenadas))
        