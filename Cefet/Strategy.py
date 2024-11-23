# Victor COculilo Desouzart

from abc import ABC, abstractmethod
import random
import time

# Interface da estrategia
class Strategy(ABC):
    @abstractmethod
    def execute(self, unit):
        pass

# Aqui estão as 4 estrategias que mudaram durante o código, a agressiva, defensiva, flanco, e aleatória
class AggressiveStrategy(Strategy):
    def execute(self, unit):
        print(f"{unit.name} vai de frente mesmo, cara a cara com o inimigo")
        unit.strength -= random.randint(1, 3)

class DefensiveStrategy(Strategy):
    def execute(self, unit):
        print(f"{unit.name} a defesa e o melhor ataque, so levantou o escudo")
        unit.strength += random.randint(1, 2)

class FlankingStrategy(Strategy):
    def execute(self, unit):
        print(f"{unit.name} vai na surdina por tras enquanto ninguem ta vendo")
        unit.strength -= random.randint(0, 1)
        unit.strength += 2  # Benefício ao flanquear

class RandomAttackStrategy(Strategy):
    def execute(self, unit):
        action = random.choice(["agressivo", "defensivo", "na espreita"])
        print(f"{unit.name} nem sabe o que ta fazendo, acabou lutando {action}.")
        unit.strength += random.randint(-2, 2)

# A classe Unit que fara a troca de estratégias dos personagens
class Unit:
    def __init__(self, name, strength, strategy: Strategy):
        self.name = name
        self.strength = strength
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy
        print(f"{self.name} alterou a estrategia para {self.strategy.__class__.__name__}.")

    def execute_strategy(self):
        print(f"\nStatus da unidade {self.name} | Forca: {self.strength}")
        self.strategy.execute(self)
        print(f"Nova forca de {self.name}: {self.strength}")

# Código para simular o jogo
if __name__ == "__main__":
    # Unidades que estarão no jogo, já com estrátegias base
    unit1 = Unit("Infantaria", 10, AggressiveStrategy())
    unit2 = Unit("Cavalaria", 12, DefensiveStrategy())
    unit3 = Unit("Arqueiro", 8, FlankingStrategy())

    # código para simular um jogo de 3 rodadas
    for round in range(3):
        print(f"\n=== Rodada {round + 1} ===")
        unit1.execute_strategy()
        unit2.execute_strategy()
        unit3.execute_strategy()
        time.sleep(1)

        # Aqui é onde o código muda a estrategia das unidades, no caso, tem 3 rodadas, pois na primeira rodada eles usam a estratégia base deles
        # na segunda eles fazem a troca de estrategia depois de usar a padrão e só na terceira aparece já usando a nova estrátegia apenas com uma linha de código set.
        if round == 1:
            unit1.set_strategy(DefensiveStrategy())
            unit2.set_strategy(FlankingStrategy())
            unit3.set_strategy(RandomAttackStrategy())

