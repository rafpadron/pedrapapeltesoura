opcoes = ["PEDRA","PAPEL","TESOURA"]
jogar = True
nome1 = input("Qual e seu nome?, jogador 1: ")
nome2 = input("Qual e seu nome?, jogador 2: ")
while jogar == True:

    usuario = input('PEDRA, PAPEL O TESOURA {}: '.format(nome1)).upper()
    usuario2 = input('PEDRA, PAPEL O TESOURA {}: '.format(nome2)).upper()

    if usuario not in opcoes or usuario2 not in opcoes:
        print('Movimiento invalido, repita')
    elif usuario == usuario2:
        print('Empate')
    elif (usuario == "PAPEL" and usuario2 == "PEDRA") or (usuario == "TESOURA" and usuario2 == "PAPEL") or (usuario == "PEDRA" and usuario2 == "TIJERAS"):
        print("Ganha {}".format(nome1))
    else:
     print("Ganha {}".format(nome2))
    
    volver = input("Você quer jogar de novo? SIM o NAO: ").upper()
    if(volver == "SIM"):
        jogar == True
    else:
        break
       
    
