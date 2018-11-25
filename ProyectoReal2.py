#-*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from random import *
import time
class Tic_tac_toe:
    """Esta clase es un tablero de un juego de triqui tiene multiples atributos y metodos
    lea a continuacion para más información"""
    def __init__(self,pos1="-",pos2="-",pos3="-",pos4="-",pos5="-",pos6="-",pos7="-",pos8="-",pos9="-"):
        """ Este es el constructor de la clase tiene como atributos cada posicion del tablero, posiciones
        que por defecto comienzan vacias"""
        self.pos0=pos1
        self.pos1=pos2
        self.pos2=pos3
        self.pos3=pos4
        self.pos4=pos5
        self.pos5=pos6
        self.pos6=pos7
        self.pos7=pos8
        self.pos8=pos9
    def lista(self):
        """Este metodo se utiliza para retornar una lista con todas las posiciones del tablero"""
        lista=[self.pos0,self.pos1,self.pos2,self.pos3,self.pos4,self.pos5,self.pos6,self.pos7,self.pos8]
        return lista
    def __str__(self):
        """Este metodo fue creado con la finalidad de revisar el codigo, se utiliza para retornar el tablero de juego 
        para así comprobar que todo este ocurriendo correctamente"""
        return (str(self.pos0)+str(self.pos1)+str(self.pos2) + "\n" +str(self.pos3)+str(self.pos4)+str(self.pos5)+"\n" +str(self.pos6)+str(self.pos7)+str(self.pos8))
    def cambiarpos(self,n,turno):
        """Este metodo funciona para cambiar los atributos de la clase, es decir cambia las posiciones del tablero
        recibe un n(posicion a cambiar) y un turno(que es el token del jugador, x o 0)"""
        if n==0:
            self.pos0=turno
        elif n==1:
            self.pos1=turno
        elif n==2:
            self.pos2=turno
        elif n==3:
            self.pos3=turno
        elif n==4:
            self.pos4=turno
        elif n==5:
            self.pos5=turno
        elif n==6:
            self.pos6=turno
        elif n==7:
            self.pos7=turno
        elif n==8:
            self.pos8=turno
        
tablero = Tic_tac_toe()
posiciones = tablero.lista()

def selectRandom(lista):
    """Esta funcion utiliza el modulo random para elegir un valor al azar entre los valores de una lista que se le pasa como 
    paramentro Esta lista puede tomar distintos valores, según la subdivision del tablero que se necesite(esquinas y medios) """
    longitud = len(lista)
    r = randrange(0, longitud)
    return lista[r]

def MovComp(wn):
    """Esta funcion tiene como finalidad predecir el mejor movimiento posible que la maquina puede utilizar.
    Primero revisa todos sus futuros posibles, y evalua en cada uno para saber si puede ganar, en el caso de que pueda elije ese futuro y gana, en el caso de que no 
    revisa todos los futuros de su oponente y evalua si el puede ganar, en el caso de que asi sea, la maquina se defendera, en el caso contrario elegira su siguiente movimiento
    con base a cual le convenga mas. esto lo logra dividiendo el tablero en tres zonas distintas donde las esquinas tienen prioridad sobre los medios y estos a su vez tienen prioridad del centro
    funciona para la mayoria de los casos exceptuando el tercer turno de la maquina donde la prioridad depende del movimiento anterior
    utiliza funciones como winning2 y selectRandom para esto"""
    posiciones=tablero.lista()
    movPosibles = [x for x, letter in enumerate(posiciones) if letter == "-"]
    movimiento = 0
    for let in ["x","0"]:
        for i in movPosibles:
            copiaPosiciones=posiciones[:]
            copiaPosiciones[i]= let
            if winning2(wn, copiaPosiciones):
                movimiento=i
                return movimiento
    esquinasVacias = []
    for i in movPosibles:
        if i in [0,2,6,8]:
            esquinasVacias.append(i)
    if len(esquinasVacias) > 0:
        movimiento = selectRandom(esquinasVacias)
        return movimiento
    if 4 in movPosibles:
        movimiento = 4
        return movimiento
    ladosVacios = []
    for i in movPosibles:
        if i in [1,3,5,7]:
            ladosVacios.append(i)
    if len(ladosVacios) > 0:
        movimiento = selectRandom(ladosVacios)
    return movimiento

def printearTablero(wn, lista):
    """Esta funcion tiene la finalidad de actualizar el canvas con las posiciones actuales de juego"""
    for pos in range(9):
        if lista[pos] != "-":
            if lista[pos] == "x":
                wn.blit(cruz,(puntosCardinales_x[pos],puntosCardinales_y[pos]))
            elif lista[pos] == "0":
                wn.blit(circulo,(puntosCardinales_x[pos],puntosCardinales_y[pos]))
        else:
            continue
def winning(wn, tablero):
    """Esta funcion toma como parametros una ventana(canvas) y un tablero, luego evalua todos las posibles victorias que se pueden dar
    esto lo logra accediendo a sus posicioes y evaluando si existe un ganador en ese tablero, en el caso de que exista manda un mensaje de victoria"""
    if tablero[0] == "0" and tablero[1] == "0" and tablero[2] == "0":
        pygame.draw.line(wn,(30,144,255),(20,100),(570,100),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif tablero[3] == "0" and tablero[4] == "0" and tablero[5] == "0":
        pygame.draw.line(wn,(30,144,255),(20,300),(570,300),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif tablero[6] == "0" and tablero[7] == "0" and tablero[8] == "0":
        pygame.draw.line(wn,(30,144,255),(20,520),(570,520),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif tablero[0] == "0" and tablero[3] == "0" and tablero[6] == "0":
        pygame.draw.line(wn,(30,144,255),(100,20),(100,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif tablero[1] == "0" and tablero[4] == "0" and tablero[7] == "0":
        pygame.draw.line(wn,(30,144,255),(300,20),(300,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif tablero[2] == "0" and tablero[5] == "0" and tablero[8] == "0":
        pygame.draw.line(wn,(30,144,255),(520,20),(520,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif tablero[0] == "0" and tablero[4] == "0" and tablero[8] == "0":
        pygame.draw.line(wn,(30,144,255),(20,20),(570,570),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    elif tablero[2] == "0" and tablero[4] == "0" and tablero[6] == "0":
        pygame.draw.line(wn,(30,144,255),(20,570),(570,20),20)
        wn.blit(circlewin,(200,200))
        estado = True
        return estado
    if tablero[0] == "x" and tablero[1] == "x" and tablero[2] == "x":
        pygame.draw.line(wn,(255,0,0),(20,100),(570,100),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif tablero[3] == "x" and tablero[4] == "x" and tablero[5] == "x":
        pygame.draw.line(wn,(255,0,0),(20,300),(570,300),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif tablero[6] == "x" and tablero[7] == "x" and tablero[8] == "x":
        pygame.draw.line(wn,(255,0,0),(20,520),(570,520),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif tablero[0] == "x" and tablero[3] == "x" and tablero[6] == "x":
        pygame.draw.line(wn,(255,0,0),(100,20),(100,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif tablero[1] == "x" and tablero[4] == "x" and tablero[7] == "x":
        pygame.draw.line(wn,(255,0,0),(300,20),(300,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif tablero[2] == "x" and tablero[5] == "x" and tablero[8] == "x":
        pygame.draw.line(wn,(255,0,0),(520,20),(520,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif tablero[0] == "x" and tablero[4] == "x" and tablero[8] == "x":
        pygame.draw.line(wn,(255,0,0),(20,20),(570,570),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    elif tablero[2] == "x" and tablero[4] == "x" and tablero[6] == "x":
        pygame.draw.line(wn,(255,0,0),(20,570),(570,20),20)
        wn.blit(cruzwin,(200,200))
        estado = True
        return estado
    estado = False
    return estado

def winning2(wn, tablero):
    """Esta funcion evalua si el tablero que se le pasa como argumento existe alguna de las 8 condiciones de victoria para x como para circulo """
    if tablero[0] == "0" and tablero[1] == "0" and tablero[2] == "0":
        estado = True
        return estado
    elif tablero[3] == "0" and tablero[4] == "0" and tablero[5] == "0":
        estado = True
        return estado
    elif tablero[6] == "0" and tablero[7] == "0" and tablero[8] == "0":
        estado = True
        return estado
    elif tablero[0] == "0" and tablero[3] == "0" and tablero[6] == "0":
        estado = True
        return estado
    elif tablero[1] == "0" and tablero[4] == "0" and tablero[7] == "0":
        estado = True
        return estado
    elif tablero[2] == "0" and tablero[5] == "0" and tablero[8] == "0":
        estado = True
        return estado
    elif tablero[0] == "0" and tablero[4] == "0" and tablero[8] == "0":
        estado = True
        return estado
    elif tablero[2] == "0" and tablero[4] == "0" and tablero[6] == "0":
        estado = True
        return estado
    if tablero[0] == "x" and tablero[1] == "x" and tablero[2] == "x":
        estado = True
        return estado
    elif tablero[3] == "x" and tablero[4] == "x" and tablero[5] == "x":
        estado = True
        return estado
    elif tablero[6] == "x" and tablero[7] == "x" and tablero[8] == "x":
        estado = True
        return estado
    elif tablero[0] == "x" and tablero[3] == "x" and tablero[6] == "x":
        estado = True
        return estado
    elif tablero[1] == "x" and tablero[4] == "x" and tablero[7] == "x":
        estado = True
        return estado
    elif tablero[2] == "x" and tablero[5] == "x" and tablero[8] == "x":
        estado = True
        return estado
    elif tablero[0] == "x" and tablero[4] == "x" and tablero[8] == "x":
        estado = True
        return estado
    elif tablero[2] == "x" and tablero[4] == "x" and tablero[6] == "x":
        estado = True
        return estado
    estado = False
    return estado

def tableroLleno():
    """ Esta funcion cuanta la cantidad de posiciones vacias en el tablero, y en el caso de que no hallan posiciones vacias, es
    decir que el tabklero este lleno retorna True, caso contrario retorna False"""
    if posiciones.count("-") == 0:
        return True
    else:
        return False

def posVacia(pos):
    """Esta funcion evalua si la posicion pos del tablero de juego se encuentra vacia"""
    if pos == "-":
        return True
    else:
        return False

def jugada(wn,tablero,jugador,item):
    """Esta funcion es utilizada para el turno del jugador humano y para la modalidad de dos jugadores, su funcionalidad es
    almacenar en las variables mx y my las cordenadas del click del jugador, luego divide por sectores el juego y evalua en que
    division esta, y la cambia a posicion ocupada"""
    posOcupada = item;
    jugadahecha = False
    if jugador == circulo:
        posOcupada = "0"
    elif jugador == cruz:
        posOcupada = "x"
    mx,my = pygame.mouse.get_pos()
    while (not jugadahecha):
        if 0 <= mx <= 205:
            if 0 <= my <= 205:
                if posVacia(posiciones[0]):
                    posiciones[0] = posOcupada
                    jugadahecha=True
            elif 206 <= my <= 390:
                if posVacia(posiciones[3]):
                    posiciones[3] = posOcupada
                    jugadahecha=True
            elif 391 <= my <= 600:
                if posVacia(posiciones[6]):
                    posiciones[6] = posOcupada
                    jugadahecha=True
        elif 206 <= mx <= 390:
            if 0 <= my <= 205:
                if posVacia(posiciones[3]):
                    posiciones[1] = posOcupada
                    jugadahecha=True
            elif 206 <= my <= 390:
                if posVacia(posiciones[4]):
                    posiciones[4] = posOcupada
                    jugadahecha=True
            elif 391 <= my <= 600:
                if posVacia(posiciones[7]):
                    posiciones[7] = posOcupada
                    jugadahecha=True
        elif 391 <= mx <= 600:
            if 0 <= my <= 205:
                if posVacia(posiciones[2]):
                    posiciones[2] = posOcupada
                    jugadahecha=True
            elif 206 <= my <= 390:
                if posVacia(posiciones[5]):
                    posiciones[5] = posOcupada
                    jugadahecha=True
            elif 391 <= my <= 600:
                if posVacia(posiciones[8]):
                    posiciones[8] = posOcupada
                    jugadahecha=True

def TicTacToe():
    """Esta es la funcion principal, esta decide la modalidad de juego y en el caso de se modalidad dos jugadores, quine iniciara, ademas es quien inicia el juego y llama a las
    demas funciones"""
    modalidad=int(raw_input("¿Que modalidad quieres jugar? Presione 1 para jugar con la maquina, o 2 para jugar de dos jugadores "))
    if(modalidad==2):
        Jugador_1 = raw_input("Quién empezara la partida: Cruz o Circulo. ")
        Jugador_1 = Jugador_1.lower()
        if Jugador_1 == "cruz":
            TurnoJugador1 = False
            Num1 = 4
            Num2 = 5
        elif Jugador_1 == "circulo":
            TurnoJugador1 = True
            Num1 = 5
            Num2 = 4
        else:
            print("Ingrese Cruz o Circulo.")
            return TicTacToe()
        wn = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Tic Tac Toe")
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
                        if not winning(wn, posiciones):
                            TurnoJugador1 = False
                            jugada(wn,tablero,circulo,"")
                            printearTablero(wn, posiciones)
                    else:
                        if not winning(wn, posiciones):
                            TurnoJugador1 = True
                            jugada(wn,tablero,cruz,"")
                            printearTablero(wn, posiciones)
                    if tableroLleno():
                        if not winning(wn, posiciones):
                            print("Empate")
            reload(wn,posiciones)
    else:
        juego(tablero,1, "")

def reload(wn,tablero):
    """Esta funcion se encarga de actualizar el tablero"""
    winning(wn,posiciones)
    pygame.draw.line(wn,white,(200,0),(200,600),10)
    pygame.draw.line(wn,white,(400,0),(400,600),10)
    pygame.draw.line(wn,white,(0,200),(600,200),10)
    pygame.draw.line(wn,white,(0,400),(600,400),10)
    pygame.display.update()

def juego(tablero, turno,movimiento):
    """Esta funcion, es la que reproduce el juego si se elige la modalidad para jugar con la maquina"""
    wn = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Tic Tac Toe")
    listaPosiciones=tablero.lista()
    esquinas = [tablero.pos0,tablero.pos2,tablero.pos6,tablero.pos8]
    if not winning(wn,listaPosiciones):
        if turno % 2 == 1:
            if turno==3:
                esquinaContraria = 8 - movimiento
                if("0" in esquinas):
                    if listaPosiciones[esquinaContraria]=="-":
                        tablero.cambiarpos(esquinaContraria,"x")
                    else:
                        movimiento=MovComp(wn)
                        tablero.cambiarpos(movimiento,"x")
                elif(tablero.pos4=="-"):
                    tablero.cambiarpos(4,"x")
                else:
                    tablero.cambiarpos(esquinaContraria,"x")
            else:
                movimiento=MovComp(wn)
                tablero.cambiarpos(movimiento,"x")
        else:
            posiciones= int(raw_input("Ingrese una posición (0-8): "))
            tablero.cambiarpos(posiciones,"0")
        reload(wn, listaPosiciones)
        printearTablero(wn, listaPosiciones)
    else:
        print("¡Tenemos un ganador!")
        printearTablero(wn, listaPosiciones)
        reload(wn, listaPosiciones)
        return
    if turno==9:
        if not winning(wn, tablero):
            printearTablero(wn, listaPosiciones)
            print("Empate")
            return
        else:
            print("¡Tenemos un ganador!")
            printearTablero(wn, listaPosiciones)
            reload(wn, listaPosiciones)
            return
    printearTablero(wn, tablero.lista())
    reload(wn, listaPosiciones)
    time.sleep(2)
    return juego(tablero, turno+1,movimiento)

pygame.init()
circlewin = pygame.image.load("CircleWin.png")
cruzwin = pygame.image.load("CruzWin.png")
circulo = pygame.image.load("Circulo.png")
cruz = pygame.image.load("Cruz.png")
white=(255,255,255)
puntosCardinales_x=[31,241,446,31,241,446,31,241,446]
puntosCardinales_y=[31,31,31,241,241,241,446,446,446]
TicTacToe()

