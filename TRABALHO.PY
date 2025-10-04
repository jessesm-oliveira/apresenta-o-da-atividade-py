# CRIE UM SIMULADOR DE LOGIN, ONDE PEDE A SENHA DO USUÁRIO, SE ELE ERRAR 3 VEZES FALE QUE A SENHA ESTÁ INCORRETA E FINALIZE O PROGRAMA.

import os # PARA LIMPAR A TELA
os.system('cls') # LIMPA A TELA
import colorama # PARA CORES
colorama.init(autoreset=True) # PARA RESETAR AS CORES AUTOMATICAMENTE
import time # PARA USAR O TIME.SLEEP

print(150*"$") # LINHA DE IGUALDADE
print("")
print(  "-----------☣️-​☣️-​☣️-​☣️-​☣️​-☣️​-☣️-​☣️​-☣️​-☣️​-☣️​-☣️​-☣️-​☣️​-☣️-​☣️-​☣️-​☣️-​☣️-​☣️-​☣️-​☣️​ ---------------> BEM VINDO AO LOGIN <---------------- ☣️-​☣️-​☣️-​☣️-​☣️​-☣️​-☣️-​☣️​-☣️​-☣️​-☣️​-☣️​-☣️-​☣️​-☣️-​☣️-​☣️-​☣️-☣️-​☣️-​") 
print("")
print(150*"$") # LINHA DE IGUALDADE

senha_correta = "123" # SENHA DO USUÁRIO
tentativas = 0 # CONTADOR DE TENTATIVAS



while tentativas < 3: # USANDO WHILE PARA CRIAR O LAÇO DE REPETIÇÃO E USANDO A VARIAVEL TENTATIVAS MENOR QUE 3 PARA LIMITAR AS TENTATIVAS 
    print("")
    nome = input(colorama.Fore.WHITE + "DIGITE O SEU NOME: -----> ") # PEDE AO USUÁRIO INSERIR O NOME 
    print("")
    senha = input(colorama.Fore.WHITE + "DIGITE A SENHA : -----> ") # PEDE AO USUÁRIO INSERIR A SENHA 
    print("")  
     
    if senha == senha_correta:
        for i in range(3): # LAÇO DE REPETIÇÃO PARA SIMULAR O ACESSO AO SISTEMA
            print("Acessando o sistema" + "😎😎😎😎😎" + "." * (i + 1)) # SIMULAÇÃO DE ACESSO AO SISTEMA
            time.sleep(1) # PAUSA DE 1 SEGUNDO
            os.system('cls') # LIMPA A TELA
          

        
        print("Login bem-sucedido!") # MENSAGEM DE LOGIN BEM-SUCEDIDO
        time.sleep(0.5) # PAUSA DE 0.5 
        os.system("cls") # LIMPA A TELA DO TERMINAL

        print("")
        print(colorama.Fore.YELLOW + "-----------------------  🌗​🌘​ VOCÊ ACESSOU O SISTEMA COM SUCESSO  🌗​🌘​ -----------------------------") # MENSAGEM DE LOGIN BEM-SUCEDIDO
        print("")
        print('----------------------------> ⚽ NOTICIAS ----------------------------') # MENSAGEM DE NOTICIAS
        print('')
        print('---------------------------->  🏋️ TENDÊNCIAS --------------------------') # MENSAGEM DE TENDÊNCIAS
        print('')
        print('----------------------------> 🔔 NOTIFICAÇÕES ------------------------') # MENSAGEM DE NOTIFICAÇÕES
        print('')
        print('----------------------------> ✉️ CONVITES  ---------------------------') # MENSAGEM DE CONVITES
        print('')
        print('----------------------------> 👨🏼REUNIÕES ----------------------------') # MENSAGEM DE REUNIÕES
        print('')


    else: # SE A SENHA ESTIVER INCORRETA
        print(colorama.Fore.RED +"Senha incorreta 🤡🤡🤡🤡") # MENSAGEM DE SENHA INCORRETA
        tentativas += 1 # ADICIONA 1 NA VARIAVEL TENTATIVAS
        time.sleep(0.5) # PAUSA DE 0.5 SEGUNDOS
        os.system('cls') # LIMPA A TELA

if tentativas == 3: # SE A VARIAVEL TENTATIVAS FOR IGUAL A 3
    print("")
    print(colorama.Fore.GREEN + "VOCÊ EXEDEU O NÚMEROS DE TENTATIVAS 😒😒😒😒") # MENSAGEM DE EXEDEU O NÚMERO DE TENTATIVAS
    print("")
    time.sleep(1.5) # PAUSA DE 1.5 SEGUNDOS
    os.system('cls') # LIMPA A TELA
    print(colorama.Fore.RED + "ACESSO NEGADO ❌❌❌❌") # MENSAGEM DE ACESSO NEGADO
    print("")
    time.sleep(1.5) # PAUSA DE 1.5 SEGUNDOS
    os.system('cls') # LIMPA A TELA
    print(colorama.Fore.YELLOW + "TENTE NOVAMENTE MAIS TARDE 😭😭😭😭") # MENSAGEM DE TENTE NOVAMENTE MAIS TARDE
    time.sleep(0.5) # PAUSA DE 0.5 SEGUNDOS

for c in range(3,-1,-1): # CONTADOR REGRESSIVO
    print('​​😑😑😑😑😑😑😑😑😑😑​ -------------------> PROGRAMA SE ENCERRANDO <------------------- 😑😑😑😑😑😑😑😑😑😑​')
    print(c) # MOSTRA O CONTADOR REGRESSIVO
    time.sleep(1) # PAUSA DE 1 SEGUNDO
    os.system('cls') # LIMPA A TELA


print(150*"$") # LINHA DE IGUALDADE
print("")
print((colorama.Fore.YELLOW + "​​​💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥​ --------->  ​PROGRAMA ENCERRADO <-------------- ​​​​​💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥​"))
print("")
print(150*"$") # LINHA DE IGUALDADE
