class NumeroUm:
    def imprimir(self):
        print("1")

def parenteses(func):
    def wrapper():
        print("(")
        func()
        print(")")
    return wrapper

def colchetes(func):
    def wrapper():
        print("[")
        func()
        print("]")
    return wrapper

def chaves(func):
    def wrapper():
        print("{")
        func()
        print("}")
    return wrapper

@parenteses
def imprimir_com_parenteses():
    numero_um = NumeroUm()
    numero_um.imprimir()

@colchetes
def imprimir_com_colchetes():
    numero_um = NumeroUm()
    numero_um.imprimir()

@chaves
def imprimir_com_chaves():
    numero_um = NumeroUm()
    numero_um.imprimir()

@colchetes
@chaves
def imprimir_com_colchetes_e_chaves():
    numero_um = NumeroUm()
    numero_um.imprimir()

@chaves
@parenteses
@colchetes
def imprimir_com_todas_as_formas():
    numero_um = NumeroUm()
    numero_um.imprimir()

imprimir_com_parenteses()  # imprime: (1)
imprimir_com_colchetes()  # imprime: [1]
imprimir_com_chaves()  # imprime: {1}
imprimir_com_colchetes_e_chaves()  # imprime: {[1]}
imprimir_com_todas_as_formas()  # imprime: {[1]}