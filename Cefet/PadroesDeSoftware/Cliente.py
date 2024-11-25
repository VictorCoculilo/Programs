#Victor Coculilo Desouzart
from Proxy import RecursoReal, Proxy

# Inicializando o recurso real e o proxy de segurança
recurso_real = RecursoReal()
proxy = Proxy(recurso_real)

# Adicionando usuários e permissões
proxy.adicionar_usuario("Alice", "adm")  # Permissão de adm
proxy.adicionar_usuario("Bob", "usuario")    # permissão de usuario, não ira funcionar
proxy.adicionar_usuario("Carlos", "adm") # Permissão de adm

# Testes
print("\nTeste 1: Usuário 'Alice' tenta acessar (esperado: SUCESSO)\n")
proxy.acessar("Alice")

print("\nTeste 2: Usuário 'Bob' tenta acessar (esperado: FALHA)\n")
proxy.acessar("Bob")

print("\nTeste 3: Usuário 'Carlos' tenta acessar (esperado: SUCESSO)\n")
proxy.acessar("Carlos")

print("\nTeste 4: Usuário 'Diana' tenta acessar (não cadastrada, esperado: FALHA)\n")
proxy.acessar("Diana")
