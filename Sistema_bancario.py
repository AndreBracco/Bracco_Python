menu = '''

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=> : '''

deposito = ""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "a":
        print("Insira o valor de deposito abaixo")
        deposito = int(input())
        if deposito <= 0:
            print("Valor de deposito inválido")
        elif deposito >=1:
            saldo += deposito
            print(f"Seu saldo é de: R$ {saldo:.2f}")
            extrato += f"Deposito no valor de R$ {deposito:.2f}\n"
           
    
    elif opcao == "b":
        print(f"Seu saldo é de R$ {saldo:.2f}\n")
        saque = float(input("Insira o valor de saque: "))
       
        excede_limite = saque > limite

        excede_tentativas = numero_saque == LIMITE_DE_SAQUES

        excede_saldo = saque > saldo


        if excede_limite:
            print("Operação inválda, valor inserido excede o limite de R$ 500,00 por saque.")

        elif valor_n_numerico:
            print("Valor inválido.")    

        elif excede_tentativas:
            print("Operação inválida, são permitidas apenas 3 operações de saque por dia.")    

        elif excede_saldo:
            print("Operação inválida, valor inserido é maior que o saldo em conta.")    

        else:
            print(f"Sacando o valor de R$ {saque:.2f}.")  
            extrato += f"Saque no valor de R$ {saque:.2f}.\n"
            saldo -= saque 
            numero_saque += 1
            print(f"Seu saldo é de R$ {saldo:.2f}.")
            tentativa = LIMITE_DE_SAQUES - numero_saque
            print(f"Você tem mais {tentativa} saque(s).")
         

    elif opcao == "c":
        print("\n============== EXTRATO ==============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "d":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")               