import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE
from random import randint

pygame.init()


def main():
    ANCHO_VENTANA = 1200
    ALTO_VENTANA = 800
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Car Carty")

    # Reloj para controlar los FPS
    reloj = pygame.time.Clock()

    # Fuente para el texto
    fuente_regular = pygame.font.SysFont(None, 70)
    fuente_botones = pygame.font.SysFont(None, 70)

    # Colores
    rojo = (255, 0, 0)
    verde = (0, 255, 0)
    blanco = (255, 255, 255)
    negro = (0, 0, 0)

    def dibujar_texto(texto, fuente, color, superficie, x, y):
        texto_renderizado = fuente.render(texto, True, color)
        rect_texto = texto_renderizado.get_rect(center=(x, y))
        superficie.blit(texto_renderizado, rect_texto)

    # llamar las imagenes de los objetos:
    carro_negro = pygame.image.load("../imagenes/black.png")
    carro_negro = pygame.transform.scale(carro_negro, (600, 300))

    carro_amarillo = pygame.image.load("../imagenes/yellow.png")
    carro_amarillo = pygame.transform.scale(carro_amarillo, (600, 300))

    carro_azul = pygame.image.load("../imagenes/blue.png")
    carro_azul = pygame.transform.scale(carro_azul, (600, 300))

    carro_rojo = pygame.image.load("../imagenes/red.png")
    carro_rojo = pygame.transform.scale(carro_rojo, (600, 300))

    bache = pygame.image.load("../imagenes/bache.png")
    bache = pygame.transform.scale(bache, (600, 300))

    # funcion para llamar a los objetos:
    def carro_negro_func(x, y):
        ventana.blit(carro_negro, (x, y))

    def loop_juego():
        condicion = False
        cambio_X = 0
        x = 280
        y = 500

        while not condicion:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    condicion = True

                # Mover el carro
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        cambio_X = -9
                    if evento.key == pygame.K_RIGHT:
                        cambio_X = 9
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        cambio_X = 0

            x += cambio_X

            # Imagen de fondo
            fondo_calle = pygame.image.load("../imagenes/escenario.png")
            fondo_calle = pygame.transform.scale(fondo_calle, (ANCHO_VENTANA, ALTO_VENTANA))
            ventana.blit(fondo_calle, (0, 0))

            carro_negro_func(x, y)
            pygame.display.update()
            reloj.tick(60)

    def menu_principal():
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Detección de clic en los botones
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mouse_x, mouse_y = evento.pos

                    if (
                            x_boton_inicio <= mouse_x <= x_boton_inicio + 170 and y_boton_menu <= mouse_y <= y_boton_menu + 60):
                        loop_juego()  # Iniciar el juego

                    if (
                            x_boton_inicio + 800 <= mouse_x <= x_boton_inicio + 800 + 170 and y_boton_menu <= mouse_y <= y_boton_menu + 60):
                        pygame.quit()  # Cerrar el juego
                        sys.exit()

                        # Botones
            x_boton_inicio = ANCHO_VENTANA / 9.5
            y_boton_menu = ALTO_VENTANA / 1.4

            # Imagen de fondo
            imagen_de_fondo = pygame.image.load("../imagenes/fondo.png")
            imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
            ventana.blit(imagen_de_fondo, (0, 0))

            # Botón inicio
            pygame.draw.rect(ventana, verde, [x_boton_inicio, y_boton_menu, 170, 60])
            dibujar_texto("Start", fuente_botones, negro, ventana, x_boton_inicio + 80, y_boton_menu + 30)

            # Botón de salir
            pygame.draw.rect(ventana, rojo, [x_boton_inicio + 800, y_boton_menu, 170, 60])
            dibujar_texto("Exit", fuente_botones, negro, ventana, x_boton_inicio + 880, y_boton_menu + 30)

            pygame.display.flip()
            reloj.tick(60)

    menu_principal()


if __name__ == "__main__":
    main()