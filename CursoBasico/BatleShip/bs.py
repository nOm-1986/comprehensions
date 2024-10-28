import random

class Barco:
    def __init__(self, model, size, symbol):
        self.model = model
        self.size = size
        self.symbol = symbol
        self.impactos = 0 

    def recibir_impacto(self):
        self.impactos += 1

    def esta_hundido(self):
        return self.impactos >= self.size

    def __repr__(self):
        return f"Barco:(Modelo='{self.model}', Tamaño='{self.size}', Simbolo='{self.symbol}')"


class Submarine(Barco):
    def __init__(self):
        super().__init__("Submarine", 2, 'S')


class Destructor(Barco):
    def __init__(self):
        super().__init__("Destructor", 3, 'D')


class Acorazado(Barco):
    def __init__(self):
        super().__init__("Acorazado", 4, 'A')


class Tablero:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.matriz = [["~" for _ in range(tamaño)] for _ in range(tamaño)]
        self.ataques_realizados = []
        self.barcos = []

    def imprimir_tablero(self):
        for fila in self.matriz:
            print(" ".join(fila))

    def colocar_barco(self, c, f, orientacion, barco):
        if not (0 <= c < self.tamaño) or not (0 <= f < self.tamaño):
            print("Coordenadas fuera de rango.")
            return False

        if orientacion == 'v':
            if c + barco.size > self.tamaño:  
                print("No hay suficiente espacio para colocar el barco verticalmente.")
                return False
            
            for i in range(barco.size):
                if self.matriz[c + i][f] != "-":
                    print("Ya hay un barco en esa posición.")
                    return False

            for i in range(barco.size):
                self.matriz[c + i][f] = barco.symbol
        
        elif orientacion == 'h':
            if f + barco.size > self.tamaño:  
                print("No hay suficiente espacio para colocar el barco horizontalmente.")
                return False
            
            for i in range(barco.size):
                if self.matriz[c][f + i] != "-":
                    print("Ya hay un barco en esa posición.")
                    return False

            for i in range(barco.size):
                self.matriz[c][f + i] = barco.symbol

        else:
            print("Orientación no válida. Use 'v' para vertical o 'h' para horizontal.")
            return False

        # Guardamos el barco y sus posiciones
        self.barcos.append((barco, [(c + i, f) if orientacion == 'v' else (c, f + i) for i in range(barco.size)]))
        
        return True
    
    def atacar(self, c, f):
        if not (0 <= c < self.tamaño) or not (0 <= f < self.tamaño):
            print("Coordenadas fuera de rango.")
            return False

        if (c, f) in self.ataques_realizados:
            print(f"Ya atacaste esta posición ({c+1}, {f+1}) antes.")
            return False

        self.ataques_realizados.append((c, f)) 

        if self.matriz[c][f] == "-":
            print("Agua!!")
        else:
            print(f"¡Golpeaste un barco en la posición ({c+1}, {f+1})!")
            # Encontrar el barco impactado
            for barco, posiciones in self.barcos:
                if (c, f) in posiciones:
                    barco.recibir_impacto()
                    if barco.esta_hundido():
                        print(f"Hundiste el barco {barco.model}!")
                    break  # Salir del bucle al encontrar el barco
            
            self.matriz[c][f] = " * "
        return True


class Player:
    def __init__(self, name):
        self.name = name
        self.tablero = Tablero()
        self.barcos_colocados = 0

    def colocar_barcos(self):
        # Colocar los barcos obligatorios
        barcos = [Destructor(), Acorazado(), Submarine()]
        
        for barco in barcos:
            colocado = False
            if self.name == "PC":
                print("turno de la computadora")
                while not colocado:
                    c = random.randint(1, 10)
                    f = random.randint(1, 10)
                    orientacion = random.choice(['v', 'h'])
                    colocado = self.tablero.colocar_barco((c-1), (f-1), orientacion, barco)
                    self.tablero.imprimir_tablero()
                    if colocado:
                        print(f"Barco {barco.model} colocado correctamente.")

            while not colocado:
                c = int(input(f"{self.name}, ingresa la fila para colocar el barco {barco.model} (tamaño {barco.size}): "))
                f = int(input(f"{self.name}, ingresa la columna para colocar el barco {barco.model}: "))
                orientacion = input(f"{self.name}, ingresa la orientación (v/h) para colocar el barco {barco.model}: ")
                colocado = self.tablero.colocar_barco((c-1), (f-1), orientacion, barco)
                self.tablero.imprimir_tablero()
                if colocado:
                    print(f"Barco {barco.model} colocado correctamente.")

    def atacar_oponente(self, oponente, c, f):
        print(f"{self.name} está atacando las coordenadas ({c}, {f}) en el tablero de {oponente.name}.")
        return oponente.tablero.atacar((c-1), (f-1))

    def ha_perdido(self):
        return all(barco[0].esta_hundido() for barco in self.tablero.barcos)


class Juego:
    def __init__(self):
        self.jugador1 = Player(input("Ingresa el nombre del Jugador 1: "))
        self.jugador2 = Player(input("Ingresa el nombre del Jugador 2, Si quieres jugar contra la computadora, ingresa PC: "))

    def iniciar(self):
        self.jugador1.colocar_barcos()
        self.jugador2.colocar_barcos()
        self.jugar()

    def jugar(self):
        while True:
            # Turno del jugador 1
            c = int(input(f"{self.jugador1.name}, ingresa la fila para atacar: "))
            f = int(input(f"{self.jugador1.name}, ingresa la columna para atacar: "))
            if self.jugador1.atacar_oponente(self.jugador2, c, f):
                if self.jugador2.ha_perdido():
                    print(f"¡{self.jugador2.name} ha perdido!")
                    break

            if self.jugador2.name == "PC":
                c = random.randint(1, 5)
                f = random.randint(1, 5)
                print(f"{self.jugador2.name} ataca en ({c}, {f})")
                if self.jugador2.atacar_oponente(self.jugador1, c, f):
                    if self.jugador1.ha_perdido():
                        print(f"¡{self.jugador1.name} ha perdido!")
                        break
            else:
                c = int(input(f"{self.jugador2.name}, ingresa la fila para atacar: "))
                f = int(input(f"{self.jugador2.name}, ingresa la columna para atacar: "))
                if self.jugador2.atacar_oponente(self.jugador1, c, f):
                    if self.jugador1.ha_perdido():
                        print(f"¡{self.jugador1.name} ha perdido!")
                        break


juego = Juego()
juego.iniciar()