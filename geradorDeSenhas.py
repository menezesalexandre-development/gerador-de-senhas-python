import string
import secrets


def gerar_senha(caracteres=20):
    todos_caracteres = string.ascii_letters + string.digits
    return ''.join(secrets.choice(todos_caracteres) for _ in range(caracteres))


print(f'Senha gerada: {gerar_senha()}')
print(f'Senha gerada: {gerar_senha()}')
print(f'Senha gerada: {gerar_senha()}')
print(f'Senha gerada: {gerar_senha()}')
print(f'Senha gerada: {gerar_senha()}')
