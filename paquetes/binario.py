class Binario():

    def __init__(self):
        pass
    
    # Algoritmo de base 10 a base 2
    def __algoritmo(self,numero):
        palabra = '' 
        while numero >= 1:
            a = int(numero) % 2
            numero = numero/2
            palabra = str(a) + palabra
        return palabra

    # Retorna el resultado del algoritmo
    def get(self,numero):
        return self.__algoritmo(numero)