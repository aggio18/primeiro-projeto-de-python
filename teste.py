while True :
    menor = 1
    maior = 1000
    tentativas = 0

    while True: 
        palpite = (menor + maior) // 2
        tentativas = tentativas + 1
        resposta = input(f"Seu numero e {palpite}? (digite 'acertou', 'maior', 'menor'):").lower()
        if resposta == "acertou":   
            print(f"Consegui! Advinhei em {tentativas} tentativas!")
            break
        elif resposta == "maior":
                menor = palpite + 1
                print(f"Nao consegui tentarei outro numero")
        elif resposta == "menor":
            maior = palpite -1
            print(f"Nao consegui tentarei outro numero")
        else:
            print("Opcao invalida! Digite apenas 'acertou', 'maior', 'menor'. ")

# Pergunta pos-jogo (fora da partida, dentro do loop principal)
    jogar_de_novo = input("Quer jogar de novo? (S/N):").lower()
    if jogar_de_novo == "n":    
         break #Encerra o programa