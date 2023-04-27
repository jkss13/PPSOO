class Nome:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class NomeFactory:
    def cria_nome(self, nome_completo):
        raise NotImplementedError

class NomeSobrenomeFactory(NomeFactory):
    def cria_nome(self, nome_completo):
        partes = nome_completo.split()
        nome = partes[0]
        sobrenome = partes[1]
        return Nome(nome, sobrenome)

class SobrenomeNomeFactory(NomeFactory):
    def cria_nome(self, nome_completo):
        partes = nome_completo.split(',')
        nome = partes[1].strip()
        sobrenome = partes[0].strip()
        return Nome(nome, sobrenome)

class AplicacaoNomes:
    def __init__(self, nome_factory):
        self.nomes = []
        self.nome_factory = nome_factory

    def adiciona_nome(self, nome_completo):
        nome = self.nome_factory.cria_nome(nome_completo)
        self.nomes.append(nome)

    def imprime_nomes(self):
        for nome in self.nomes:
            print(f"{nome.nome} {nome.sobrenome}")

# Exemplo de uso
nome_sobrenome_factory = NomeSobrenomeFactory()
sobrenome_nome_factory = SobrenomeNomeFactory()

app1 = AplicacaoNomes(nome_sobrenome_factory)
app1.adiciona_nome("Joao Silva")
app1.adiciona_nome("Maria Santos")

app2 = AplicacaoNomes(sobrenome_nome_factory)
app2.adiciona_nome("Silva, Joao")
app2.adiciona_nome("Santos, Maria")

app1.imprime_nomes()
app2.imprime_nomes()