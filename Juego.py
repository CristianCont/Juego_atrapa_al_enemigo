import pygame 
import sys
import random

# Constantes
Ancho = 800
Alto = 600
Color_rojo = (255, 0, 0)
Color_negro = (0, 0, 0)
Color_verde = (0, 255, 0)
Fuente_color = (255, 255, 255)
# Jugador 
jugador_size = 50
jugador_pos = [Ancho / 2, Alto - jugador_size * 2]
contador_atrapar = 0  
atrapar_contada = False  

# Enemigo
Enemigo_size = 50
Enemigo_pos = [random.randint(0, Ancho - Enemigo_size), 0]

# Ventana 
ventana = pygame.display.set_mode((Ancho, Alto))
pygame.font.init()
fuente = pygame.font.SysFont('Arial', 30)
game_over = False
clock = pygame.time.Clock()

def detectar_choque(jugador_pos, enemigo_pos):
    jx = jugador_pos[0]
    jy = jugador_pos[1]
    ex = enemigo_pos[0]
    ey = enemigo_pos[1]
    
    if (ex >= jx and ex < (jx + jugador_size)) or (jx >= ex and jx < (ex + Enemigo_size)):
        if (ey >= jy and ey < (jy + jugador_size)) or (jy >= ey and jy < (ey + Enemigo_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = jugador_pos[0]
            if event.key == pygame.K_LEFT:
                x -= jugador_size
            if event.key == pygame.K_RIGHT:
                x += jugador_size
            jugador_pos[0] = x
    
    ventana.fill(Color_negro)
    
    if Enemigo_pos[1] >= 0 and Enemigo_pos[1] < Alto:
        Enemigo_pos[1] += 20
    else:
        Enemigo_pos[0] = random.randint(0, Ancho - Enemigo_size)
        Enemigo_pos[1] = 0
        atrapar_contada = False  

    if detectar_choque(jugador_pos, Enemigo_pos) and not atrapar_contada:
        contador_atrapar += 1 
       
        atrapar_contada = True  
        
    # Dibujar Enemigo
    pygame.draw.rect(ventana, Color_rojo, (Enemigo_pos[0], Enemigo_pos[1], jugador_size, jugador_size))
    
    # Dibujar jugador
    pygame.draw.rect(ventana, Color_verde, (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
     # Mostrar contador en la parte superior derecha
    texto = fuente.render("Enemigo Atrapado: " + str(contador_atrapar), True, Fuente_color)
    ventana.blit(texto, (Ancho - texto.get_width() - 10, 10))
    clock.tick(20)
    pygame.display.update()