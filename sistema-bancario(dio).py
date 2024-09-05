print('-=' * 20)  # Imprime uma linha decorativa
print(F'{"BANCO".center(40)}')  # Centraliza e imprime o título "BANCO"
print('-=' * 20)  # Imprime outra linha decorativa

# Inicialização de variáveis
saque = 0  # Armazena o valor total de saques realizados
valor_limite_de_saque = 500  # Limite máximo de saque por operação
extrato = 0  # Saldo atual da conta
numero_de_saque = 0  # Contador de saques realizados
limite_de_saque = 3  # Limite de saques permitidos por dia
numero_de_deposito = 0  # Contador de depósitos realizados
transacoes = []  # Lista para armazenar as transações

# Menu do banco que será exibido ao usuário
menu = '''
[S] Para Saque
[D] Para Depósito 
[E] Para Extrato
[Q] Para Sair
'''
print(menu)  # Exibe o menu de opções

while True:
    # Solicita ao usuário que escolha uma das opções do menu
    escolha = input('Escolha uma das opções acima! ').upper().strip()[0]

    # Condicional para operação de saque
    if escolha == 'S':
        print('-' * 40)  # Linha decorativa
        print(f'{"SAQUE".center(40)}')  # Centraliza e imprime o título "SAQUE"
        print('-' * 40)  # Linha decorativa
        
        if limite_de_saque > 0:  # Verifica se ainda há saques disponíveis
            valor_saque = float(input('Qual o valor do Saque? R$'))  # Solicita o valor do saque
            
            # Verifica se o valor do saque é válido e dentro do limite diário
            if valor_saque > 0 and valor_saque <= 500:
                # Verifica se há saldo suficiente para o saque
                if valor_saque <= extrato:
                    saque += valor_saque  # Adiciona o valor ao total de saques
                    extrato -= valor_saque  # Subtrai o valor do saldo
                    numero_de_saque += 1  # Incrementa o contador de saques
                    limite_de_saque -= 1  # Decrementa o limite de saques disponíveis
                    transacoes.append(f'Saque de R${valor_saque:.2f}')  # Registra a transação no extrato
                    
                    # Confirmação de saque realizado
                    print(f'Saque de R${valor_saque:.2f} realizado com sucesso')
                    print(f'Saldo atual: R${extrato:.2f}')  # Exibe o saldo atual
                    print(f'Limite de saques restantes: {limite_de_saque}')  # Exibe o limite de saques restantes
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                # Mensagem de erro para valor de saque acima do limite diário
                print('Valor passa do limite diário de R$500.00 ')
        else:
            # Mensagem informando que o limite de saques foi atingido
            print('Você atingiu o limite máximo de saque,\n Permitido por dia!')
        print('-' * 40)  # Linha decorativa

    # Condicional para operação de depósito
    elif escolha == 'D':
        print('-' * 40)  # Linha decorativa
        print(f'{"DEPÓSITO".center(40)}')  # Centraliza e imprime o título "DEPÓSITO"
        print('-' * 40)  # Linha decorativa
        
        valor_deposito = float(input('Qual o valor do deposito? R$'))  # Solicita o valor do depósito
        
        # Validação para impedir depósito de valores negativos
        while valor_deposito < 0:
            print('Valor não permitido! Tente novamente')  # Mensagem de erro
            valor_deposito = float(input('Qual o valor do deposito? R$'))  # Solicita o valor do depósito novamente
        
        if valor_deposito > 0:  # Verifica se o valor do depósito é válido
            extrato += valor_deposito  # Adiciona o valor ao saldo
            numero_de_deposito += 1  # Incrementa o contador de depósitos
            transacoes.append(f'Depósito de R${valor_deposito:.2f}')  # Registra a transação no extrato
            
            # Confirmação de depósito realizado
            print(f'Depósito de R${valor_deposito:.2f} Realizado com Sucesso')
        print('-' * 40)  # Linha decorativa

    # Condicional para exibir o extrato
    elif escolha == 'E':
        print('-' * 40)  # Linha decorativa
        print(f'{"EXTRATO".center(40)}')  # Centraliza e imprime o título "EXTRATO"
        print('-' * 40)  # Linha decorativa
        
        if not transacoes:  # Verifica se não há transações registradas
            print('Não foram realizadas transações.')
        else:
            for transacao in transacoes:  # Itera sobre a lista de transações
                print(transacao)  # Exibe cada transação registrada
        
        # Exibe o saldo atual
        print(f'Saldo Atual: R${extrato:.2f}')
        print('-' * 40)  # Linha decorativa

    # Condicional para sair do sistema
    elif escolha == 'Q':
        print('-=' * 20)  # Linha decorativa
        print(f'{"Saindo do sistema...Até a próxima!".center(40)}')  # Mensagem de saída
        print('-=' * 20)  # Linha decorativa
        break  # Encerra o loop e sai do programa

    # Mensagem de erro para opção inválida
    else:
        print('-' * 40)  # Linha decorativa
        print('Opção Invalida! Por favor tente novamente!')  # Mensagem de erro
        print('-' * 40)  # Linha decorativa
