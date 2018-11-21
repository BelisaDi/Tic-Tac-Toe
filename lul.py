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
    def lista(self):
        lista=[self.pos0,self.pos1,self.pos2,self.pos3,self.pos4,self.pos5,self.pos6,self.pos7,self.pos8]
        return lista
    def __str__(self):
        return (str(self.pos0)+str(self.pos1)+str(self.pos2) + "\n" +str(self.pos3)+str(self.pos4)+str(self.pos5)+"\n" +str(self.pos6)+str(self.pos7)+str(self.pos8))
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
def posVacia(pos): #Revisa si la posicion está vacia
    if pos == "-":
        return True
    else:
        return False
def winning(posiciones): #Comprueba las condiciones de victoria
    
    if posiciones[0] == "0" and posiciones[1] == "0" and posiciones[2] == "0":
        estado = True
        return estado
    elif posiciones[3] == "0" and posiciones[4] == "0" and posiciones[5] == "0":
        estado = True
        return estado
    elif posiciones[6] == "0" and posiciones[7] == "0" and posiciones[8] == "0":
        estado = True
        return estado
    elif posiciones[0] == "0" and posiciones[3] == "0" and posiciones[6] == "0":
        estado = True
        return estado
    elif posiciones[1] == "0" and posiciones[4] == "0" and posiciones[7] == "0":
        estado = True
        return estado
    elif posiciones[2] == "0" and posiciones[5] == "0" and posiciones[8] == "0":
        estado = True
        return estado
    elif posiciones[0] == "0" and posiciones[4] == "0" and posiciones[8] == "0":
        estado = True
        return estado
    elif posiciones[2] == "0" and posiciones[4] == "0" and posiciones[6] == "0":
        estado = True
        return estado
    if posiciones[0] == "x" and posiciones[1] == "x" and posiciones[2] == "x":
        estado = True
        return estado
    elif posiciones[3] == "x" and posiciones[4] == "x" and posiciones[5] == "x":
        estado = True
        return estado
    elif posiciones[6] == "x" and posiciones[7] == "x" and posiciones[8] == "x":
        estado = True
        return estado
    elif posiciones[0] == "x" and posiciones[3] == "x" and posiciones[6] == "x":
        estado = True
        return estado
    elif posiciones[1] == "x" and posiciones[4] == "x" and posiciones[7] == "x":
        estado = True
        return estado
    elif posiciones[2] == "x" and posiciones[5] == "x" and posiciones[8] == "x":
        estado = True
        return estado
    elif posiciones[0] == "x" and posiciones[4] == "x" and posiciones[8] == "x":
        estado = True
        return estado
    elif posiciones[2] == "x" and posiciones[4] == "x" and posiciones[6] == "x":
        estado = True
        return estado
    estado = False
    return estado
def MovComp(tablero):
    posiciones=tablero.lista()
    movPosibles = [x for x, letter in enumerate(posiciones) if letter == "-"]
    movimiento = 0
    for let in ["x","0"]:
        for i in movPosibles:     
            copiaPosiciones = posiciones[:]
            copiaPosiciones[i] = let
            if winning(copiaPosiciones):
                movimiento = i
                return movimiento
    esquinasVacias = [] 
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
        movimiento = selectRandom(ladosVacios)
    return movimiento
    
def selectRandom(lista):  #Para que seleccione aleatoriamente una esquina o lado.
    longitud = len(lista)
    r = randrange(0, longitud)
    return lista[r]
def buscarEsquinas(tablero):
    posiciones = tablero.lista()
    esquinas = [posiciones[0],posiciones[2],posiciones[6],posiciones[8]]
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
def juego(tablero,jugador1,turno,movimiento):
    print("El turno es: ",turno)
    listaPosiciones=tablero.lista()
    print(listaPosiciones)
    if not winning(listaPosiciones):
        if turno % 2 == 1:
            if turno==3:
                esquinaContraria = 8 - movimiento
                if listaPosiciones[esquinaContraria]=="-":
                    tablero.cambiarpos(esquinaContraria,"x")
                    print(esquinaContraria)
                else:
                     movimiento=MovComp(tablero)
                     tablero.cambiarpos(movimiento,"x")
            else:      
                movimiento=MovComp(tablero)
                tablero.cambiarpos(movimiento,"x")
            print(tablero)
        else:
            posiciones= int(input("Posicion?"))
            tablero.cambiarpos(posiciones,"0")
    else:
        print("Ganooooooooooooooooooooooooooooooooooooooooooooo")
        return
    if turno==9:
        print("Empate")
        return
    return juego(tablero, jugador1, turno+1,movimiento)

tablero=Tic_tac_toe("-","-","-","-")
juego(tablero, "machine", 1,0)