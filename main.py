from random import randint

def imprimirTabuleiro():
  print (tabuleiro[0] + " | " + tabuleiro[1]  + " | " + tabuleiro[2])
  print ("‾‾‾‾‾‾‾‾‾")
  print (tabuleiro[3] + " | " + tabuleiro[4]  + " | " + tabuleiro[5])
  print ("‾‾‾‾‾‾‾‾‾")
  print (tabuleiro[6] + " | " + tabuleiro[7]  + " | " + tabuleiro[8])

def jogarNovamente():
  resposta = input('Digite "S" para jogar novamente: ')
  if (resposta.lower() != "s"):
    return False
  else:
    return True

def checaVencedor():
  for combinacao in condicoesVitoria:
    if ((tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]]) and (tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]])):
      for j in jogador:
        if (j["simbolo"] == tabuleiro[combinacao[0]]):
          j["vitorias"] += 1
          print(j["nome"] + "(" + j["simbolo"] + ") foi a vencedor (Vitórias: " + str(j["vitorias"]) + ")")
          return True
  return False

condicoesVitoria = ([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6])
jogador = [{"nome":"","vitorias":0,"simbolo":"X","turno":False},{"nome":"","vitorias":0,"simbolo":"O","turno":False}]
jogador[0]["nome"] = input('Digite o nome do jogador 1 (X):')
jogador[1]["nome"] = input('Digite o nome do jogador 2 (O):')

while True:
  rodada = 0
  tabuleiro = ["1","2","3","4","5","6","7","8","9"]
  print('----------- Jogo da velha -----------')
  if (randint(0,1) == 0):
    jogador[0]["turno"] = True
    print (jogador[0]["nome"] + " começa jogando!")
  else:
    jogador[1]["turno"] = True
    print (jogador[1]["nome"] + " começa jogando!")

  imprimirTabuleiro()

  while rodada <= 8:
    for j in jogador:
      if (j["turno"] is True):
        while True:
          jogada = input(j['nome'] + ", digite uma posição para " + j['simbolo'] + " :")
          if ((jogada in tabuleiro ) and (jogada not in ("X","x","o","O"))):
            break
          else:
            print ('Digite uma jogada válida!')
        tabuleiro[int(jogada) - 1] = j['simbolo']
        j['turno'] = False
        imprimirTabuleiro()
      else:
        j['turno'] = True
    if((rodada >= 4) and (checaVencedor())):
      break
    else:
      rodada += 1
  if(not(jogarNovamente())):
    break