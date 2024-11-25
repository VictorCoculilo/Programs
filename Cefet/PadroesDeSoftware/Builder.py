#Victor Coculilo Desouzart
from abc import ABC, abstractmethod

# Classe pedido
class Pedido:
    def __init__(self, pao, carne, queijo, bacon, molho, salada, cebola):
        self.pao = pao
        self.carne = carne
        self.queijo = queijo
        self.bacon = bacon
        self.molho = molho
        self.salada = salada
        self.cebola = cebola


# Classe do Hamburguer que vai ser construido
class Hamburguer:
    def __init__(self):
        self.componentes = []

    def adicionar(self, componente):
        self.componentes.append(componente)

    def __str__(self):
        return "\n".join(self.componentes)


# Builder genérico que vai implementar os outros 2 builders
class HamburguerBuilder(ABC):
    def __init__(self):
        self.hamburguer = Hamburguer()

    def get_hamburguer(self):
        return self.hamburguer

    @abstractmethod
    def construir_pao(self, pao):
        pass

    @abstractmethod
    def construir_carne(self, carne):
        pass

    @abstractmethod
    def construir_queijo(self, queijo):
        pass

    @abstractmethod
    def construir_bacon(self, bacon):
        pass

    @abstractmethod
    def construir_molho(self, molho):
        pass

    @abstractmethod
    def construir_salada(self, salada):
        pass

    @abstractmethod
    def construir_cebola(self, cebola):
        pass


# Builder preguiçoso, um dos dois casos da implementação do builder
class HamburguerBuilderPreguiçoso(HamburguerBuilder):
    def construir_pao(self, pao):
        self.hamburguer.adicionar(f"Pão: só botou uma fatia de {pao}")

    def construir_carne(self, carne):
        self.hamburguer.adicionar(f"Carne: {carne}g de hamburguer meio desmontado")

    def construir_queijo(self, queijo):
        self.hamburguer.adicionar(f"Queijo: Talvez seja {queijo}")

    def construir_bacon(self, bacon):
        self.hamburguer.adicionar(f"Bacon: arremessou {bacon}g")

    def construir_molho(self, molho):
        self.hamburguer.adicionar(f"Molho: {molho} ou barbecue")

    def construir_salada(self, salada):
        self.hamburguer.adicionar(f"Salada: faltou {salada}")

    def construir_cebola(self, cebola):
        self.hamburguer.adicionar(f"Cebola: esqueceu de cortar a {cebola}")


# Builder veganp, segundo caso da implementação do builder
class HamburguerBuilderVegano(HamburguerBuilder):
    def construir_pao(self, pao):
        self.hamburguer.adicionar(f"Pão: trocou {pao} por integral")

    def construir_carne(self, carne):
        self.hamburguer.adicionar(f"Carne: {carne}g de carne de soja")

    def construir_queijo(self, queijo):
        self.hamburguer.adicionar(f"Queijo: jogou o {queijo} e colocou tofu")

    def construir_bacon(self, bacon):
        self.hamburguer.adicionar(f"Bacon: nem pensar")

    def construir_molho(self, molho):
        self.hamburguer.adicionar(f"Molho: {molho} vegano")

    def construir_salada(self, salada):
        self.hamburguer.adicionar(f"Salada: MUITA {salada}")

    def construir_cebola(self, cebola):
        self.hamburguer.adicionar(f"Cebola: para dar o gosto uma {cebola}")


# Classe Diretor, aqui é onde ele pega o pedido e quando ele for chamado vai ser passado para o builder expecifico
class Diretor:
    def __init__(self, builder):
        self.builder = builder

    def construir_hamburguer(self, pedido):
        self.builder.construir_pao(pedido.pao)
        self.builder.construir_carne(pedido.carne)
        self.builder.construir_queijo(pedido.queijo)
        self.builder.construir_bacon(pedido.bacon)
        self.builder.construir_molho(pedido.molho)
        self.builder.construir_salada(pedido.salada)
        self.builder.construir_cebola(pedido.cebola)
        return self.builder.get_hamburguer()


# Classe Cliente, aqui ele cria um pedido e passa para o diretor o builder que ele vai usar
class Cliente:
    def fazer_pedido(self):
        # Criei meu pedido com o que eu quero no meu hamburguer
        pedido = Pedido(pao="Brioche", carne=160, queijo="Mussarela", bacon=50, molho="Maionese", salada="Alface e Tomate", cebola="Cebola Roxa")

        # Primeiro teste com o preguiçoso:
        
        # Criação de um builder preguiçoso
        builder_preguiçoso = HamburguerBuilderPreguiçoso()
        # Criação do diretor passando o builder preguiçoso para ele
        diretor = Diretor(builder_preguiçoso)
        # Aqui o diretor vai mandar constuir o hamburguer passando o pedido
        hamburguer_preguiçoso = diretor.construir_hamburguer(pedido)
        print("Hambúrguer preguiçoso:\n", hamburguer_preguiçoso)

        # Segunda teste com o vegano:
        
        # Criação de um builder vegano
        builder_vegano = HamburguerBuilderVegano()
        # Criação do diretor passando o builder vegano para ele
        diretor = Diretor(builder_vegano)
        # Aqui o diretor vai mandar constuir o hamburguer passando o pedido
        hamburguer_vegano = diretor.construir_hamburguer(pedido)
        print("\nHambúrguer Vegano:\n", hamburguer_vegano)


# Executando o cliente para rodar o código
cliente = Cliente()
cliente.fazer_pedido()
