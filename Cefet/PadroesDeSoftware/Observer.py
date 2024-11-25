# Victor Coculilo Desouzart
# O cinema é o publisher
class Cinema:
    def __init__(self):
        self._subscribers = []
        self._new_movie = None

    #adicionar novo observer
    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    #remover observer
    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    #notificar observers
    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self._new_movie)

    #lançar filme e notificar os observers
    def release_new_movie(self, movie):
        self._new_movie = movie
        print(f"\n[Cinema] Estreia, o maior sucesso de bilheteria: {movie}")
        self.notify_subscribers()

#Streaming são os observers
class Streaming:
    def __init__(self, name):
        self._name = name

    # cinema lança um filme
    def update(self, movie):
        print(f"{self._name} já sabe que '{movie}' está em cartaz no cinema.")

# Classe Cliente
class Cliente:
    def main():
        #aqui é a criação do publisher
        cinema = Cinema()

        #são 3 obeservers
        netflix = Streaming("Netflix")
        amazon_prime = Streaming("Amazon Prime")
        disney_plus = Streaming("Disney Plus")

        cinema.add_subscriber(netflix)
        cinema.add_subscriber(amazon_prime)
        cinema.add_subscriber(disney_plus)

        #lançamento de um filme
        print("\nTESTE 1: Novo filme lançado")
        cinema.release_new_movie("Synecdoche, New York")
        
        # Removendo um streaming e testando de novo
        print("\nTESTE 2: foi removido um streaming e lançamento de outro filme.")
        cinema.remove_subscriber(amazon_prime)
        cinema.release_new_movie("Interestelar")

Cliente.main()
