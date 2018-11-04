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

def wining(wn,tablero):
    if tablero.pos1 == 0 and tablero.pos2 == 0 and tablero.pos3 == 0:
        pygame.draw.line(wn,(30,144,255),(20,100),(570,100),20)
        wn.blit(circlewin,(200,200))
        return
    elif tablero.pos4 == 0 and tablero.pos5 == 0 and tablero.pos6 == 0:
        pygame.draw.line(wn,(30,144,255),(20,300),(570,300),20)
        wn.blit(circlewin,(200,200))
        return
    elif tablero.pos7 == 0 and tablero.pos8 == 0 and tablero.pos9 == 0:
        pygame.draw.line(wn,(30,144,255),(20,520),(570,520),20)
        wn.blit(circlewin,(200,200))
        return
    elif tablero.pos1 == 0 and tablero.pos4 == 0 and tablero.pos7 == 0:
        pygame.draw.line(wn,(30,144,255),(100,20),(100,570),20)
        wn.blit(circlewin,(200,200))
        return
    elif tablero.pos2 == 0 and tablero.pos5 == 0 and tablero.pos8 == 0:
        pygame.draw.line(wn,(30,144,255),(300,20),(300,570),20)
        wn.blit(circlewin,(200,200))
        return
    elif tablero.pos3 == 0 and tablero.pos6 == 0 and tablero.pos9 == 0:
        pygame.draw.line(wn,(30,144,255),(520,20),(520,570),20)
        wn.blit(circlewin,(200,200))
        return
    elif tablero.pos1 == 0 and tablero.pos5 == 0 and tablero.pos9 == 0:
        pygame.draw.line(wn,(30,144,255),(20,20),(570,570),20)
        wn.blit(circlewin,(200,200))
        return
    elif tablero.pos3 == 0 and tablero.pos5 == 0 and tablero.pos7 == 0:
        pygame.draw.line(wn,(30,144,255),(20,570),(570,20),20)
        wn.blit(circlewin,(200,200))
        return
    if tablero.pos1 == 1 and tablero.pos2 == 1 and tablero.pos3 == 1:
        pygame.draw.line(wn,(255,0,0),(20,100),(570,100),20)
        wn.blit(cruzwin,(200,200))
        return
    elif tablero.pos4 == 1 and tablero.pos5 == 1 and tablero.pos6 == 1:
        pygame.draw.line(wn,(255,0,0),(20,300),(570,300),20)
        wn.blit(cruzwin,(200,200))
        return
    elif tablero.pos7 == 1 and tablero.pos8 == 1 and tablero.pos9 == 1:
        pygame.draw.line(wn,(255,0,0),(20,520),(570,520),20)
        wn.blit(cruzwin,(200,200))
        return
    elif tablero.pos1 == 1 and tablero.pos4 == 1 and tablero.pos7 == 1:
        pygame.draw.line(wn,(255,0,0),(100,20),(100,570),20)
        wn.blit(cruzwin,(200,200))
        return
    elif tablero.pos2 == 1 and tablero.pos5 == 1 and tablero.pos8 == 1:
        pygame.draw.line(wn,(255,0,0),(300,20),(300,570),20)
        wn.blit(cruzwin,(200,200))
        return
    elif tablero.pos3 == 1 and tablero.pos6 == 1 and tablero.pos9 == 1:
        pygame.draw.line(wn,(255,0,0),(520,20),(520,570),20)
        wn.blit(cruzwin,(200,200))
        return
    elif tablero.pos1 == 1 and tablero.pos5 == 1 and tablero.pos9 == 1:
        pygame.draw.line(wn,(255,0,0),(20,20),(570,570),20)
        wn.blit(cruzwin,(200,200))
        return
    elif tablero.pos3 == 1 and tablero.pos5 == 1 and tablero.pos7 == 1:
        pygame.draw.line(wn,(255,0,0),(20,570),(570,20),20)
        wn.blit(cruzwin,(200,200))
        return

def jugada(wn,tablero,jugador):
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
                wn.blit(jugador,(31,31))
                tablero.pos1 = posOcupada
                jugadahecha=True
            elif 230 <= my <= 360:
                wn.blit(jugador,(31,241))
                tablero.pos4 = posOcupada
                jugadahecha=True
            elif 420 <= my <= 580:
                wn.blit(jugador,(31,446))
                tablero.pos7 = posOcupada
                jugadahecha=True
        elif 230 <= mx <= 360:
            if 10 <= my <= 180:
                wn.blit(jugador,(241,31))
                tablero.pos2 = posOcupada
                jugadahecha=True
            elif 230 <= my <= 360:
                wn.blit(jugador,(241,241))
                tablero.pos5 = posOcupada
                jugadahecha=True
            elif 420 <= my <= 580:
                wn.blit(jugador,(241,446))
                tablero.pos8 = posOcupada
                jugadahecha=True
        elif 420 <= mx <= 580:
            if 10 <= my <= 180:
                wn.blit(jugador,(446,31))
                tablero.pos3 = posOcupada
                jugadahecha=True
            elif 230 <= my <= 360:
                wn.blit(jugador,(446,241))
                tablero.pos6 = posOcupada
                jugadahecha=True
            elif 420 <= my <= 580:
                wn.blit(jugador,(446,446))
                tablero.pos9 = posOcupada
                jugadahecha=True

def TicTacToe():
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
    tablero = Tic_tac_toe()

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
                    if JugadasCirculo < Num1:
                            JugadasCirculo += 1
                            TurnoJugador1 = False
                            jugada(wn,tablero,circulo)
                else:
                    if JugadasCruz < Num2:
                            JugadasCruz += 1
                            TurnoJugador1 = True
                            jugada(wn,tablero,cruz)
        wining(wn,tablero)
        pygame.draw.line(wn,white,(200,0),(200,600),10)
        pygame.draw.line(wn,white,(400,0),(400,600),10)
        pygame.draw.line(wn,white,(0,200),(600,200),10)
        pygame.draw.line(wn,white,(0,400),(600,400),10)
        pygame.display.update()

TicTacToe()
