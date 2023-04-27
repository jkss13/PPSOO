from abc import ABC, abstractmethod

class PizzaFactory(ABC):
    @abstractmethod
    def criar_massa(self):
        pass

    @abstractmethod
    def adicionar_molho(self):
        pass

    @abstractmethod
    def adicionar_recheio(self):
        pass

class CalabresaPizzaFactory(PizzaFactory):
    def criar_massa(self):
        return "massa comum"

    def adicionar_molho(self):
        return "molho de tomate"

    def adicionar_recheio(self):
        return "queijo, calabresa e tomate"

class PresuntoPizzaFactory(PizzaFactory):
    def criar_massa(self):
        return "massa comum"

    def adicionar_molho(self):
        return "molho de tomate"

    def adicionar_recheio(self):
        return "queijo, presunto e tomate"

class CalzoneFactory(ABC):
    @abstractmethod
    def criar_massa(self):
        pass

    @abstractmethod
    def adicionar_molho(self):
        pass

    @abstractmethod
    def adicionar_recheio(self):
        pass

class CalabresaCalzoneFactory(CalzoneFactory):
    def criar_massa(self):
        return "massa de calzone"

    def adicionar_molho(self):
        return "molho de tomate"

    def adicionar_recheio(self):
        return "queijo, calabresa e tomate"

class PresuntoCalzoneFactory(CalzoneFactory):
    def criar_massa(self):
        return "massa de calzone"

    def adicionar_molho(self):
        return "molho de tomate"

    def adicionar_recheio(self):
        return "queijo, presunto e tomate"


class PizzaConsumer:
    def __init__(self, factory):
        self.factory = factory

    def pedir_pizza(self):
        massa = self.factory.criar_massa()
        molho = self.factory.adicionar_molho()
        recheio = self.factory.adicionar_recheio()
        return f"Pizza de {recheio} com massa de {massa} e molho de {molho}."

class CalzoneConsumer:
    def __init__(self, factory):
        self.factory = factory

    def pedir_calzone(self):
        massa = self.factory.criar_massa()
        molho = self.factory.adicionar_molho()
        recheio = self.factory.adicionar_recheio()
        return f"Calzone de {recheio} com massa de {massa} e molho de {molho}."


def main():
    # cria as fábricas de pizza e calzone
    calabresa_pizza_factory = CalabresaPizzaFactory()
    presunto_pizza_factory = PresuntoPizzaFactory()

    calabresa_calzone_factory = CalabresaCalzoneFactory()
    presunto_calzone_factory = PresuntoCalzoneFactory()

    # cria os clientes
    segunda_cliente = PizzaConsumer(calabresa_pizza_factory)
    terca_cliente = PizzaConsumer(presunto_pizza_factory)
    quarta_cliente = PizzaConsumer(calabresa_pizza_factory)
    quinta_cliente = PizzaConsumer(presunto_pizza_factory)
    sexta_cliente = PizzaConsumer(calabresa_pizza_factory)
    sabado_cliente = PizzaConsumer(presunto_pizza_factory)

    calabresa_cliente = CalzoneConsumer(calabresa_calzone_factory)
    presunto_cliente = CalzoneConsumer(presunto_calzone_factory)

    # solicita as pizzas ou calzones de acordo com o dia
    dia = input("Digite a data (dd/mm/yyyy): ")
    dia_semana = datetime.datetime.strptime(dia, '%d/%m/%Y').weekday()
    if dia_semana == 0:
        print(segunda_cliente.pedir_pizza())
    elif dia_semana == 1:
        print(terca_cliente.pedir_pizza())
    elif dia_semana == 2:
        print(quarta_cliente.pedir_pizza())
    elif dia_semana == 3:
        print(quinta_cliente.pedir_pizza())
    elif dia_semana == 4:
        print(sexta_cliente.pedir_pizza())
    elif dia_semana == 5:
        print(sabado_cliente.pedir_pizza())
    else:
        print("A pizzaria está fechada.")

    # solicita o calzone de acordo com o dia
    dia = input("Digite a data (dd/mm/yyyy): ")
    dia_semana = datetime.datetime.strptime(dia, '%d/%m/%Y').weekday()
    if dia_semana in [0, 2, 4]:
        print(calabresa_cliente.pedir_calzone())
    elif dia_semana in [1, 3, 5]:
        print(presunto_cliente.pedir_calzone())
    else:
        print("A pizzaria está fechada.")


if __name__ == '__main__':
    pizzaria = None
    opcao = input("Deseja pedir uma pizza (P) ou um calzone (C)? ").lower()
    
    if opcao == "p":
        tipo_pizza = input("Qual pizza deseja? Calabresa (C) ou Presunto (P)? ").lower()
        if tipo_pizza == "c":
            pizzaria = CalabresaPizzaFactory()
        elif tipo_pizza == "p":
            pizzaria = PresuntoPizzaFactory()
        else:
            print("Opção inválida!")
            exit()
        pizza = PizzaConsumer(pizzaria)
        print("Pedindo pizza...")
        print(f"Massa: {pizza.fazer_massa()}")
        print(f"Molho: {pizza.adicionar_molho()}")
        print(f"Recheio: {pizza.adicionar_recheio()}")
    elif opcao == "c":
        tipo_calzone = input("Qual calzone deseja? Calabresa (C) ou Presunto (P)? ").lower()
        if tipo_calzone == "c":
            pizzaria = CalabresaCalzoneFactory()
        elif tipo_calzone == "p":
            pizzaria = PresuntoCalzoneFactory()
        else:
            print("Opção inválida!")
            exit()
        calzone = CalzoneConsumer(pizzaria)
        print("Pedindo calzone...")
        print(f"Massa: {calzone.fazer_massa()}")
        print(f"Recheio: {calzone.adicionar_recheio()}")
    else:
        print("Opção inválida!")
        exit()
