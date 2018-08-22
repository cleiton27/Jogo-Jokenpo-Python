from random import randint
from time import sleep

def resultado():
    print('----------')
    print('O jogador ganhou {} veze(s)'.format(player))
    print('O computador ganhou {} veze(s)'.format(pc))
    print('Aconteceu {} empate(s)'.format(empate))

def jogarDeNovo():
    return resete()

def resete():
    print('----------')
    resete = int(input('[1]SIM [2]NÃO\nJogar novamente? '))
    if resete == 1:
        return usuario
        #Falta implementar a reinicialização do jogo

    elif resete == 2:
        return resultado()
    else:
        print('----------')
        print('Opção Inválida')
        return jogarDeNovo()

print('##### JOKENPÔ #####')

usuario = int(input('[1] - PEDRA:\n[2] - PAPEL:\n[3] - TESOURA:\nFaça sua jogada: '))
print('JÓ..')
sleep(0.8)
print('KEN..')
sleep(0.8)
print('PÔ')
print('####################')

computador = randint(1, 3)
player = int()
pc = int()
empate = int()


if usuario == 1 and computador == 1:
    print('Você escolheu PEDRA')
    print('O computador escolheu PEDRA')
    print('Jogo EMPATADO')
    empate += 1
    resete()

elif usuario == 2 and computador == 1:
     print('Você escolheu PAPEL')
     print('O computador escolheu PEDRA')
     print('Você GANHOU')
     player += 1
     resete()

elif usuario == 3 and computador == 1:
     print('Você escolheu TESOURA')
     print('Ocomputador escolheu PEDRA')
     print('Pc GANHOU')
     pc += 1
     resete()

elif usuario == 1 and computador == 2:
     print('Você escolheu PEDRA')
     print('O computador escolheu PAPEL')
     print('Pc GANHOU')
     pc += 1
     resete()

elif usuario == 2 and computador == 2:
     print('Você escolheu PAPEL')
     print('O computador escolheu PAPEL')
     print('Jogo EMPATADO')
     empate += 1
     resete()

elif usuario == 3 and computador == 2:
     print('Você escolheu TESOURA')
     print('Ocomputador escolheu PAPEL')
     print('Você GANHOU')
     player += 1
     resete()

elif usuario == 1 and computador == 3:
     print('Você escolheu PEDRA')
     print('O computador escolheu TESOURA')
     print('Você GANHOU')
     player += 1
     resete()

elif usuario == 2 and computador == 3:
     print('Você escolheu PAPEL')
     print('O computador escolheu TESOURA')
     print('Pc GANHOU')
     pc += 1
     resete()

elif usuario == 3 and computador == 3:
     print('Você escolheu TESOURA')
     print('Ocomputador escolheu TESOURA')
     print('Jogo EMPATADO')
     empate += 1
     resete()

else:
    print('Movimento INVALIDO')




