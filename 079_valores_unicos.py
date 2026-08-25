# Cria uma lista vazia para armazenar os valores digitados
valores = []

# Define 'S' como resposta inicial para entrar no while
resp = 'S'


# Enquanto a resposta for 'S', o programa continuará pedindo valores
while resp == 'S':

    # Solicita um número ao usuário e transforma o valor digitado em inteiro
    numero = int(input('Digite um valor: '))

    # Verifica se o número ainda não existe na lista
    if numero not in valores:

        # Adiciona o número à lista
        valores.append(numero)

        print('Valor adicionado com sucesso...')

    else:
        # Caso o número já esteja na lista, não adiciona novamente
        print('Valor duplicado! Não vou adicionar...')

    # Pergunta ao usuário se deseja continuar
    # upper() transforma a resposta em maiúscula
    # strip() remove espaços antes e depois da resposta
    resp = input('Quer continuar? [S/N]: ').upper().strip()

    # Enquanto a resposta não for S nem N, solicita uma nova resposta
    while resp != 'S' and resp != 'N':
        resp = input(
            'Valor inválido! Digite novamente! [S/N]: '
        ).upper().strip()


# Organiza os valores da lista em ordem crescente
valores.sort()

# Exibe uma linha de separação
print('-=' * 30)

# Mostra todos os valores únicos digitados em ordem crescente
print(f'Você digitou os valores {valores}')
