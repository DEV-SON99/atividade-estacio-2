# Inicialização da variável de saída
saida = ''

# Função para adição
def adicao(a, b):
    return a + b

# Função para subtração
def subracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função para a calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço principal
while saida.lower() != 'n':
    # Entrada dos dados
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos.")
        continue

    operacao = input("Digite a operação desejada (+, -, *, / ou adicao, subracao, multiplicacao, divisao): ")

    # Chama a função calculadora e armazena o resultado
    resultado = calculadora(num1, num2, operacao)
    
    # Exibe o resultado
    print(f'Resultado da operação: {resultado}')
    
    # Pergunta ao usuário se deseja continuar
    saida = input("Deseja continuar? (S/N): ")
    while saida.lower() not in ['s', 'n']:
        saida = input("Resposta inválida. Deseja continuar? (S/N): ")
