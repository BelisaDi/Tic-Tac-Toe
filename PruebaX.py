from random import *
class Tic_tac_toe:
    def __init__(self,pos1="-",pos2="-",pos3="-",pos4="-",pos5="-",pos6="-",pos7="-",pos8="-",pos9="-"):
        self.pos0=pos1
        self.pos1=pos2
        self.pos2=pos3
        self.pos3=pos4
        self.pos4=pos5
        self.pos5=pos6
        self.pos6=pos7
        self.pos7=pos8
        self.pos8=pos9
    def tomardecision(self,estado):
        print(estado)
    def __str__(self):
        return (str(self.pos0)+str(self.pos1)+str(self.pos2) + "\n" +str(self.pos3)+str(self.pos4)+str(self.pos5)+"\n" +str(self.pos6)+str(self.pos7)+str(self.pos8))
    def lista(self):
        lista=[self.pos0,self.pos1,self.pos2,self.pos3,self.pos4,self.pos5,self.pos6,self.pos7,self.pos8]
        return lista
    def cambiarpos(self,n,turno):
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

def juego(tablero,jugador1,jugador2,turno,decision):
    posiciones = tablero.lista()
    centro = posiciones[4]
    ocentro = False
    oesquinas = False
    omedios = False
    esquinas = [posiciones[0],posiciones[2],posiciones[6],posiciones[8]]
    medios = [posiciones[1],posiciones[3],posiciones[5],posiciones[7]]
    jugada = False
    print(esquinas)
    if turno == 9:
        return
    else:
        if turno % 2 == 1:
            if turno == 1:
                decision = choice([0,2,6,8])
                tablero.cambiarpos(decision,"x")
            if turno == 3:
                if "0" in esquinas:
                    esquinaContraria = 8 - decision
                    oesquinas = True
                    if posiciones[esquinaContraria] == "-":
                        tablero.cambiarpos(esquinaContraria,"x")
                    else:
                        cont = 0
                        for decisiones in esquinas:
                            cont += 1
                            if decisiones =="-":
                                if cont == 1:
                                    tablero.cambiarpos(0,"x")
                                    break
                                elif cont == 2:
                                    tablero.cambiarpos(2,"x")
                                    break
                                elif cont == 3:
                                    tablero.cambiarpos(6,"x")
                                    break
                                elif cont == 4:
                                    tablero.cambiarpos(8,"x")
                                    break
                elif "0" in medios:
                    omedios = True
                    tablero.cambiarpos(4,"x")
                else:
                    ocentro = True
                    tablero.cambiarpos(8,"x")
            if turno == 5:
                print("¿O en esquinas? ",oesquinas)
                print("¿O en centro? ",ocentro)
                print("¿O en lados? ",omedios)
                if oesquinas == True:
                    cont = 0
                    for decisiones in esquinas:
                        cont += 1
                        if decisiones =="-":
                            if cont == 1:
                                tablero.cambiarpos(0,"x")
                                break
                            elif cont == 2:
                                tablero.cambiarpos(2,"x")
                                break
                            elif cont == 3:
                                tablero.cambiarpos(6,"x")
                                break
                            elif cont == 4:
                                tablero.cambiarpos(8,"x")
                                break
                    if posiciones[4]=="-":
                        tablero.cambiarpos(4,"x")
                        return tablero
                elif omedios==True:
                    if tablero[esquinaContraria]=="-":
                        tablero.cambiarpos(esquinaContraria,"x")
                    else:
                        esquinaInicial=8-esquinaContraria
                        if esquinaInicial==0 or esquinaInicial== 6:
                            tablero.cambiarpos(esquinaContraria-2,"x")
                        else:
                            tableo.cambiarpos(esquinaContraria+2,"x")

            if posiciones[1] == "-" or posiciones[3] == "-" or posiciones[5] == "-" or posiciones[8] == "-":
                print("asa")
            print(tablero)
        else:
            pleiyada=int(input("Posicion"))
            if posiciones[pleiyada] == "-":
                tablero.cambiarpos(pleiyada,"0")
            else:
                print("La posición está ocupada, escoja otra.")
                return juego(tablero,"machine","human",turno,decision)
        print("El turno es: ",turno)
    return juego(tablero,"machine","human",turno+1,decision)

tokenJugadoruno = "x"
tokenJugadordos = "0"
tableros = []
tablero = Tic_tac_toe("-","-","-","-","-","-","-","-","-")

tableros = juego(tablero,"machine","human",1,"")
print(tableros)
