import pygame, sys
from pygame.locals import *

pygame.init()
circlewin = pygame.image.load("CircleWin.png")
cruzwin = pygame.image.load("CruzWin.png")
circulo = pygame.image.load("Circulo.png")
cruz = pygame.image.load("Cruz.png")

class Tic_tac_toe:
    def __init__(self,pos1="-",pos2="-",pos3="-",pos4="-",pos5="-",pos6="-",pos7="-",pos8="-",pos9="-"):
        self.pos1=pos1
        self.pos2=pos2
        self.pos3=pos3
        self.pos4=pos4
        self.pos5=pos5
        self.pos6=pos6
        self.pos7=pos7
        self.pos8=pos8
        self.pos9=pos9
    def tomarDesicion(estado):
        print(estado)
    def __str__(self):
        return (str(self.pos1)+str(self.pos2)+str(self.pos3) + "\n" +str(self.pos4)+str(self.pos5)+str(self.pos6)+ "\n" +str(self.pos7)+str(self.pos8)+str(self.pos9))

tablero = Tic_tac_toe()
global pos1
global pos2
global pos3
global pos4
global pos5
global pos6
global pos7
global pos8
global pos9

pos1 = tablero.pos1
pos2 = tablero.pos2
pos3 = tablero.pos3
pos4 = tablero.pos4
pos5 = tablero.pos5
pos6 = tablero.pos6
pos7 = tablero.pos7
pos8 = tablero.pos8
pos9 = tablero.pos9
posiciones = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9] #No sé krnal la lista con las posiciones del tablero

def winning(wn,tablero): #Comprueba las condiciones de victoria
    if posiciones[0] == 0 and posiciones[1] == 0 and posiciones[2] == 0:
        pygame.draw.line(wn,(30,144,255),(20,100),(570,100),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif posiciones[3] == 0 and posiciones[4] == 0 and posiciones[5] == 0:
        pygame.draw.line(wn,(30,144,255),(20,300),(570,300),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif posiciones[6] == 0 and posiciones[7] == 0 and posiciones[8] == 0:
        pygame.draw.line(wn,(30,144,255),(20,520),(570,520),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif posiciones[0] == 0 and posiciones[3] == 0 and posiciones[6] == 0:
        pygame.draw.line(wn,(30,144,255),(100,20),(100,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif posiciones[1] == 0 and posiciones[4] == 0 and posiciones[7] == 0:
        pygame.draw.line(wn,(30,144,255),(300,20),(300,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif posiciones[2] == 0 and posiciones[5] == 0 and posiciones[8] == 0:
        pygame.draw.line(wn,(30,144,255),(520,20),(520,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif posiciones[0] == 0 and posiciones[4] == 0 and posiciones[8] == 0:
        pygame.draw.line(wn,(30,144,255),(20,20),(570,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif posiciones[2] == 0 and posiciones[4] == 0 and posiciones[6] == 0:
        pygame.draw.line(wn,(30,144,255),(20,570),(570,20),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    if posiciones[0] == 1 and posiciones[1] == 1 and posiciones[2] == 1:
        pygame.draw.line(wn,(255,0,0),(20,100),(570,100),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif posiciones[3] == 1 and posiciones[4] == 1 and posiciones[5] == 1:
        pygame.draw.line(wn,(255,0,0),(20,300),(570,300),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif posiciones[6] == 1 and posiciones[7] == 1 and posiciones[8] == 1:
        pygame.draw.line(wn,(255,0,0),(20,520),(570,520),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif posiciones[0] == 1 and posiciones[3] == 1 and posiciones[6] == 1:
        pygame.draw.line(wn,(255,0,0),(100,20),(100,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif posiciones[1] == 1 and posiciones[4] == 1 and posiciones[7] == 1:
        pygame.draw.line(wn,(255,0,0),(300,20),(300,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif posiciones[2] == 1 and posiciones[5] == 1 and posiciones[8] == 1:
        pygame.draw.line(wn,(255,0,0),(520,20),(520,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif posiciones[0] == 1 and posiciones[4] == 1 and posiciones[8] == 1:
        pygame.draw.line(wn,(255,0,0),(20,20),(570,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif posiciones[2] == 1 and posiciones[4] == 1 and posiciones[6] == 1:
        pygame.draw.line(wn,(255,0,0),(20,570),(570,20),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    estado = False
    return estado

def tableroLleno(): #Revisa si el tablero pos ya no da más
    if posiciones.count("-") == 0:
        return True
    else:
        return False

def posVacia(pos): #Revisa si la posicion está vacia
    if pos == "-":
        return True
    else:
        return False

def jugada(wn,tablero,jugador): #Realiza las jugadas
    posOcupada = -1
    jugadahecha = False
    if jugador == circulo:
        posOcupada = 0
    elif jugador == cruz:
        posOcupada = 1
    mx,my = pygame.mouse.get_pos()
    while (not jugadahecha):
        if 10 <= mx <= 180:
            if 10 <= my <= 180:
                if posVacia(posiciones[0]):
                    wn.blit(jugador,(31,31))
                    pos1 = posOcupada
                    posiciones[0] = pos1
                    jugadahecha=True
            elif 230 <= my <= 360:
                if posVacia(posiciones[3]):
                    wn.blit(jugador,(31,241))
                    pos4 = posOcupada
                    posiciones[3] = pos4
                    jugadahecha=True
            elif 420 <= my <= 580:
                if posVacia(posiciones[6]):
                    wn.blit(jugador,(31,446))
                    pos7 = posOcupada
                    posiciones[6] = pos7
                    jugadahecha=True
        elif 230 <= mx <= 360:
            if 10 <= my <= 180:
                if posVacia(posiciones[3]):
                    wn.blit(jugador,(241,31))
                    pos2 = posOcupada
                    posiciones[1] = pos2
                    jugadahecha=True
            elif 230 <= my <= 360:
                if posVacia(posiciones[4]):
                    wn.blit(jugador,(241,241))
                    pos5 = posOcupada
                    posiciones[4] = pos5
                    jugadahecha=True
            elif 420 <= my <= 580:
                if posVacia(posiciones[7]):
                    wn.blit(jugador,(241,446))
                    pos8 = posOcupada
                    posiciones[7] = pos8
                    jugadahecha=True
        elif 420 <= mx <= 580:
            if 10 <= my <= 180:
                if posVacia(posiciones[2]):
                    wn.blit(jugador,(446,31))
                    pos3 = posOcupada
                    posiciones[2] = pos3
                    jugadahecha=True
            elif 230 <= my <= 360:
                if posVacia(posiciones[5]):
                    wn.blit(jugador,(446,241))
                    pos6 = posOcupada
                    posiciones[5] = pos6
                    jugadahecha=True
            elif 420 <= my <= 580:
                if posVacia(posiciones[8]):
                    wn.blit(jugador,(446,446))
                    pos9 = posOcupada
                    posiciones[8] = pos9
                    jugadahecha=True

def TicTacToe(): #Corre el juego
    Jugador_1 = input("Quién empezara la partida: Cruz o Circulo. ")
    if Jugador_1 == "cruz":
        TurnoJugador1 = False
        Num1 = 4
        Num2 = 5
    elif Jugador_1 == "circulo":
        TurnoJugador1 = True
        Num1 = 5
        Num2 = 4
    else:
        print("Ingrese Cruz o Circulo, no otras maricadas.")
        return TicTacToe()

    wn = pygame.display.set_mode((600,600))
    pygame.display.set_caption("This is a proof.")
    white = (255,255,255)
    JugadasCirculo = 0
    JugadasCruz = 0

    while True:
        jugadahecha=False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if TurnoJugador1 == True:
                    if not tableroLleno():
                            TurnoJugador1 = False
                            jugada(wn,tablero,circulo)
                            print(posiciones)
                else:
                    if not tableroLleno():
                            TurnoJugador1 = True
                            jugada(wn,tablero,cruz)
                            print(posiciones)
        winning(wn,tablero)
        pygame.draw.line(wn,white,(200,0),(200,600),10)
        pygame.draw.line(wn,white,(400,0),(400,600),10)
        pygame.draw.line(wn,white,(0,200),(600,200),10)
        pygame.draw.line(wn,white,(0,400),(600,400),10)
        pygame.display.update()

#TicTacToe()

def MovComp(): #Movimiento del computador (Se supone, no lo he probado.)
    movPosibles = [x for x, letter in enumerate(posiciones) if letter == "-"]
    movimiento = 0
    for let in [1,0]: #Primero revisa si se puede mover a un sitio en donde gane la cruz o el circulo, supongo que
        for i in movPosibles:      # depende de quién sea la maquina
            copiaPosiciones = posiciones[:]
            copiaPosiciones[i] = let
            if winning(wn,copiaPosiciones):
                movimiento = i
                return movimiento
    esquinasVacias = [] #Si no puede ganar, se va a una esquina
    for i in movPosibles:
        if i in [0,2,6,8]:
            esquinasVacias.append(i)
    if len(esquinasVacias) > 0:
        movimiento = selectRandom(esquinasVacias)
        return movimiento
    if 4 in movPosibles:  #Si no hay esquinas, al centro
        movimiento = 4
        return movimiento
    ladosVacios = []
    for i in movPosibles: #Si no, pos a los lados.
        if i in [1,3,5,7]:
            ladosVacios.append(i)
    if len(ladosVacios) > 0:
        movimiento = selectRandom(esquinasVacias)
    return movimiento

def selectRandom(lista):  #Para que seleccione aleatoriamente una esquina o lado.
    import random
    longitud = len(lista)
    r = random.randrange(0, longitud)
    return lista[r]

MovComp()
