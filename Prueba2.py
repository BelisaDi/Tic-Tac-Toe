import pygame, sys
from pygame.locals import *

pygame.init()

def TicTacToe():
    Jugador1 = input("Quién empezara la partida: Cruz o Circulo. ")
    if Jugador1 == "Cruz":
        TurnoJugador1 = False
        Num1 = 4
        Num2 = 5
    elif Jugador1 == "Circulo"  :
        TurnoJugador1 = True
        Num1 = 5
        Num2 = 4
    else:
        print("Ingrese Cruz o Circulo, no otras maricadas.")
        return TicTacToe()

    wn = pygame.display.set_mode((600,600))
    pygame.display.set_caption("This is a proof.")
    white = (255,255,255)
    circulo = pygame.image.load("Circulo.png")
    cruz = pygame.image.load("Cruz.png")

    JugadasCirculo = 0
    JugadasCruz = 0
    pos1 = -1
    pos2 = -1
    pos3 = -1
    pos4 = -1
    pos5 = -1
    pos6 = -1
    pos7 = -1
    pos8 = -1
    pos9 = -1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if TurnoJugador1 == True:
                    if JugadasCirculo < Num1:
                        mx,my = pygame.mouse.get_pos()
                        if 10 <= mx <= 180:
                            if 10 <= my <= 180:
                                wn.blit(circulo,(31,31))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos1 = 0
                                continue
                            elif 230 <= my <= 360:
                                wn.blit(circulo,(31,241))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos4 = 0
                                continue
                            elif 420 <= my <= 580:
                                wn.blit(circulo,(31,446))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos7 = 0
                                continue
                        elif 230 <= mx <= 360:
                            if 10 <= my <= 180:
                                wn.blit(circulo,(241,31))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos2 = 0
                                continue
                            elif 230 <= my <= 360:
                                wn.blit(circulo,(241,241))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos5 = 0
                                continue
                            elif 420 <= my <= 580:
                                wn.blit(circulo,(241,446))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos8 = 0
                                continue
                        elif 420 <= mx <= 580:
                            if 10 <= my <= 180:
                                wn.blit(circulo,(446,31))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos3 = 0
                                continue
                            elif 230 <= my <= 360:
                                wn.blit(circulo,(446,241))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos6 = 0
                                continue
                            elif 420 <= my <= 580:
                                wn.blit(circulo,(446,446))
                                JugadasCirculo += 1
                                TurnoJugador1 = False
                                pos9 = 0
                else:
                    if JugadasCruz < Num2:
                        mx,my = pygame.mouse.get_pos()
                        if 10 <= mx <= 180:
                            if 10 <= my <= 180:
                                wn.blit(cruz,(31,31))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos1 = 1
                                continue
                            elif 230 <= my <= 360:
                                wn.blit(cruz,(31,241))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos4 = 1
                                continue
                            elif 420 <= my <= 580:
                                wn.blit(cruz,(31,446))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos7 = 1
                                continue
                        elif 230 <= mx <= 360:
                            if 10 <= my <= 180:
                                wn.blit(cruz,(241,31))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos2 = 1
                                continue
                            elif 230 <= my <= 360:
                                wn.blit(cruz,(241,241))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos5 = 1
                                continue
                            elif 420 <= my <= 580:
                                wn.blit(cruz,(241,446))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos8 = 1
                                continue
                        if 420 <= mx <= 580:
                            if 10 <= my <= 180:
                                wn.blit(cruz,(446,31))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos3 = 1
                                continue
                            elif 230 <= my <= 360:
                                wn.blit(cruz,(446,241))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos6 = 1
                                continue
                            elif 420 <= my <= 580:
                                wn.blit(cruz,(446,446))
                                JugadasCruz += 1
                                TurnoJugador1 = True
                                pos9 = 1
        if pos1 == 0:
            if pos2 == 0 and pos3 == 0:
                print("Circulo gana.")
                break
            elif pos4 == 0 and pos7 == 0:
                print("Circulo gana.")
                break
            elif pos5 == 0 and pos9 == 0:
                print("Circulo gana.")
                break
        if pos5 == 0:
            if pos4 == 0 and pos6 == 0:
                print("Circulo gana.")
                break
            elif pos2 == 0 and pos8 == 0:
                print("Circulo gana.")
                break
            elif pos3 == 0 and pos7 == 0:
                print("Circulo gana.")
                break
        if pos9 == 0:
            if pos7 == 0 and pos8 == 0:
                print("Circulo gana.")
                break
            elif pos3 == 0 and pos6 == 0:
                print("Circulo gana.")
                break

        if pos1 == 1:
            if pos2 == 1 and pos3 == 1:
                print("Cruz gana.")
                break
            elif pos4 == 1 and pos7 == 1:
                print("Cruz gana.")
                break
            elif pos5 == 1 and pos9 == 1:
                print("Cruz gana.")
                break
        if pos5 == 1:
            if pos4 == 1 and pos6 == 1:
                print("Cruz gana.")
                break
            elif pos2 == 1 and pos8 == 1:
                print("Cruz gana.")
                break
            elif pos3 == 1 and pos7 == 1:
                print("Cruz gana.")
                break
        if pos9 == 1:
            if pos7 == 1 and pos8 == 1:
                print("Cruz gana.")
                break
            elif pos3 == 1 and pos6 == 1:
                print("Cruz gana.")
                break
        pygame.draw.line(wn,white,(200,0),(200,600),10)
        pygame.draw.line(wn,white,(400,0),(400,600),10)
        pygame.draw.line(wn,white,(0,200),(600,200),10)
        pygame.draw.line(wn,white,(0,400),(600,400),10)
        pygame.display.update()
TicTacToe()
