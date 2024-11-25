#Victor Coculilo Desouzart
from abc import ABC, abstractmethod

# Interface para o recurso sensível
class RecursoSensivel(ABC):
    @abstractmethod
    def acessar(self):
        pass


# Aqui é onde irá dar acesso real ao recurso sensivel
class RecursoReal(RecursoSensivel):
    def acessar(self):
        print("Acessando recurso sensível...")


# Implementação do padrão Proxy que vai controlar os acessos
class Proxy(RecursoSensivel):
    def __init__(self, recurso_real):
        self._recurso_real = recurso_real
        self._usuarios_permitidos = {}  # Uma lista com todos os usuarios permitidos

    def adicionar_usuario(self, usuario, permissao):
        
        # Metodo para adicionar um usuário e tambem com seu nível de permissão
       
        self._usuarios_permitidos[usuario] = permissao

    def acessar(self, usuario):
    
        # Verifica as permissões do usuário antes de conceder acesso.
        
        print(f"Solicitação de acesso pelo usuário: {usuario}")
        if usuario in self._usuarios_permitidos and self._usuarios_permitidos[usuario] == "adm": #se não tiver permissão adm, será recusado
            print(f"Acesso concedido ao usuário: {usuario}")
            self._registrar_acesso(usuario, sucesso=True)
            self._recurso_real.acessar()
        else:
            print(f"Acesso negado ao usuário: {usuario}")
            self._registrar_acesso(usuario, sucesso=False)

    def _registrar_acesso(self, usuario, sucesso):
        
        # Registra o acesso no console.
       
        status = "SUCESSO" if sucesso else "FALHA"
        print(f"Registro de acesso - Usuário: {usuario}, Status: {status}")
