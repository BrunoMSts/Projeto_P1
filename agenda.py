import sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'


def printCores(texto, cor) :
  print(cor + texto + RESET)

#FEITO-------------------------------------------------
def adicionar(descricao, extras):
  if descricao  == '' :
    return False
  else:
    novaAtividade = ''
    a = 0
    for i in itens:
      while a != len(i[1]):
        if i[1][a] != '':
          novaAtividade += i[1][a] + ' '
        if a == 2:
          novaAtividade += descricao
        a += 1
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(novaAtividade + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False

  return True


#FEITO-----------------------------------
def prioridadeValida(pri):
  if len(pri) == 3 and pri[0] == '(' and 'A' <= pri[1] <= 'Z' and pri[2] == ')':
    return True
  else:
    return False


#FEITO------------------------------------
def horaValida(horaMin):
  if len(horaMin) == 4 and soDigitos(horaMin) and int(horaMin[:2]) < 24 and int(horaMin[2:]) < 60: #USANDO SLICE FACILITA A COMPARAÇÃO 
    return True
  else:
    return False
#FEITO--------------------------------------
def dataValida(data):
  if len(data) == 8 and soDigitos(data):
    dia = int(data[:2])
    mes = int(data[2:4])
    if mes == 2 and 0 < dia <= 29:
      return True
    if mes != 2:
      if (mes % 2 == 0) and (0 < dia <= 30):
        return True
      elif (mes != 2 and mes % 2 != 0) and (0 < dia <= 31):
        return True
      else:
        return False
    else:
      return False
  return False

#FEITO--------------------------------- 
def projetoValido(proj):
  if len(proj) >= 2 and proj[0] == '+':
    return True
  else:
    return False

#FEITO--------------------------------------------
def contextoValido(cont):
  if len(cont) >= 2 and cont[0] == '@':
    return True
  else:
    return False
    
def soDigitos(numero):
  if type(numero) != str:
    return False
  for x in numero:
    if x < '0' or x > '9':
      return False
  return True

#FEITO-------------------------------------------------------
def organizar(linhas):
  global itens
  itens = []
  for l in linhas:
    data = '' 
    hora = ''
    pri = ''
    desc = ''
    contexto = ''
    projeto = ''
  
    l = l.strip() # remove espaços em branco e quebras de linha do começo e do fim
    tokens = l.split() # quebra o string em palavras
    if dataValida(tokens[0]):
      data = tokens.pop(0)
    if horaValida(tokens[0]):
      hora = tokens.pop(0)
    if prioridadeValida(tokens[0].upper()):
      pri = tokens.pop(0).upper()
    if projetoValido(tokens[-1]):
      projeto = tokens.pop()
    if contextoValido(tokens[-1]):
      contexto = tokens.pop()
    for i in tokens:
      desc += i + ' '
    itens.append((desc, (data, hora, pri, contexto, projeto)))
  return itens

def listar(var='n'):
  try:
    fp = open(TODO_FILE, 'r')
    linhas = fp.readlines()
    conteudo = organizar(linhas)
    atividades = {}
    conteudo = ordenarPorPrioridade(ordenarPorDataHora(conteudo))
    for index in range(len(conteudo)):
      atividades[index+1] = conteudo[index]
    if var != 'n':
      return atividades
    for key,values in atividades.items():
      a, at = 0, ''
      while a != len(values[1]):
        if values[1][a] != '':
          if dataValida(values[1][a]):
            at += values[1][a][:2] + '/' + values[1][a][2:4] + '/' + values[1][a][4:] + ' '
          elif horaValida(values[1][a]):
            at += values[1][a][:2] + 'h' + values[1][a][2:4] + 'm' + values[1][a][4:] + ' '
          else:
            at += values[1][a] + ' '
        if a == 2:
          at += values[0]
        a += 1
      atividades[key] = at
    for keys, values in atividades.items():
      if '(A)' in values and conteudo[keys-1][1][2] == '(A)':
        print(keys,': ', end='')
        printCores(values, RED)
      elif '(B)' in values and conteudo[keys-1][1][2] == '(B)':
        print(keys,': ', end='')
        printCores(values, GREEN)
      elif '(C)' in values and conteudo[keys-1][1][2] == '(C)':
        print(keys,': ', end='')
        printCores(values, YELLOW)
      elif '(D)' in values and conteudo[keys-1][1][2] == '(D)':
        print(keys,': ', end='')
        printCores(values, BLUE)
      else:
        print(keys,':', values)
  except IOError:
    print('Não possui nenhuma atividade registrada!')

def inverterData(data):
  data = int(data[4:] + data[2:4] + data[:2])
  return data

def ordenarPorDataHora(itens):
  semDatas, semHora = [], []
  d,h = 0,0
  
  while d != len(itens): #REMOVE AS ATIVIDADES QUE NÃO TEM DATA PARA PODER INSERIR NO FINAL...
    if itens[d][1][0] == '':
      semDatas.append(itens.pop(d))
      d -= 1
    d += 1
  while h != len(itens): #REMOVE AS ATIVIDADES QUE NÃO TEM HORA.., PARA PODER ADICIONAR AO FINAL..
    if itens[h][1][1] == '':
      semHora.append(itens.pop(h))
      h -= 1
    h += 1
  for c in range(len(semDatas)):
    for c1 in range(len(semDatas)):
      if semDatas[c][1][1] != '' and semDatas[c1][1][1] != '':
        if int(semDatas[c][1][1]) < int(semDatas[c1][1][1]):
          aux = semDatas[c1]
          semDatas[c1] = semDatas[c]
          semDatas[c] = aux

  for h in range(len(semHora)): #INSERINDO NO FINAL AS ATIVIDADES QUE NAO TEM HORA
    for h1 in range(len(semHora)):
      if semHora[h][1][0] != '' and semHora[h1][1][0] != '':
        if inverterData(semHora[h][1][0]) < inverterData(semHora[h1][1][0]):
          aux = semHora[h1]
          semHora[h1] = semHora[h]
          semHora[h] = aux  
  for a in range(len(itens)): #VEZES QUE O FOR VAI REPETIR
    for b in range(len(itens)):
      if inverterData(itens[a][1][0]) < inverterData(itens[b][1][0]): #COMPARA O PRIMEIRO COM O RESTO, E DEPOIS O PRÓXIMO COM O RESTO, E ASSIM VAI... 
        aux = itens[b]
        itens[b] = itens[a]
        itens[a] = aux
      elif inverterData(itens[a][1][0]) == inverterData(itens[b][1][0]): #SE AS DATAS FOREM IGUAIS, COMPARA AS HORAS...
        if itens[a][1][1] != '' and itens[b][1][1] != '':
          if int(itens[a][1][1]) < int(itens[b][1][1]):
            aux = itens[b]
            itens[b] = itens[a]
            itens[a] = aux

  for date in semHora:
    itens.append(date)

  for hour in semDatas:
    itens.append(hour)

  return itens
   
def ordenarPorPrioridade(itens):
  semPri = []
  i = 0
  while i != len(itens):
    if itens[i][1][2] == '': #REMOVE OS ITENS QUE NÃO TEM PRIORIDADE...
      semPri.append(itens.pop(i))
      i -= 1
    i += 1
  for repeticoes in range(len(itens)):
    for indices in range(len(itens)-1):
      if itens[indices][1][2] > itens[indices+1][1][2]:
        aux = itens[indices]
        itens[indices] = itens[indices+1]
        itens[indices+1] = aux
  for s in semPri:
    itens.append(s)
  return itens

def fazer(num):
  todo = open(TODO_FILE,'r')
  linhas = todo.readlines()
  todo.close()
  variavel, verificador = listar('s'), False #{1: dsadasdas, 2:dsadasdas}
  if num < 0:
    print('O número precisa ser um valor positivo')
  else:
    if num != 0 and num <= len(variavel):
      for a in range(len(linhas)):
        done = open(ARCHIVE_FILE, 'a')
        if variavel[num] == organizar([linhas[a]])[0]:
          done.write(linhas.pop(a))
          verificador = True
          break
      done.close()
      if verificador:
        todo = open(TODO_FILE, 'w')
        for i in linhas:
            todo.write(i)
        todo.close()
    else:
      print('Erro')

def remover():
  fp = open(TODO_FILE, 'r')
  linhas = fp.readlines()
  fp.close()
  variavel, verificador = listar('s'), False
  try:
    num = int(sys.argv[0])
    if num != 0 and num <= len(variavel):
      for a in range(len(linhas)):
        if variavel[num] == organizar([linhas[a]])[0]:
            linhas.pop(a)
            verificador = True
            break
      if verificador:
        fp = open(TODO_FILE, 'w')
        for i in linhas:
            fp.write(i)
        fp.close()
    else:
      print('ERRO, você ja removeu todas as atividades!')
  except ValueError:
    print('Index precisa ser um inteiro')

def priorizar(num, prioridade):
  todo = open(TODO_FILE, 'r')
  linhas = todo.readlines()
  todo.close()
  pivo = listar('s') 
  if int(num) == 0 or int(num) > len(pivo):
    print('Você não pode priorizar um item que você não adicionou!')
  else:
    var, verificador = list(pivo[int(num)][1]), False
    pivoAux2 = [pivo[int(num)][:1] + (tuple(var),)]
    var[2] = prioridade.upper()
    pivoAux = [pivo[int(num)][:1] + (tuple(var),)]
    atividade, atividadeAux = '', ''.strip()
    a,b = 0,0
    while a != len(pivoAux[0][1]):
      if pivoAux[0][1][a] != '':
        atividade += pivoAux[0][1][a] + ' '
      if a == 3:
        atividade += pivoAux[0][0] + ' '
      a += 1
    while b != len(pivoAux2[0][1]):
      if pivoAux2[0][1][b] != '':
        atividadeAux += pivoAux2[0][1][b] + ' '
      if b == 3:
        atividadeAux += pivoAux2[0][0] + ' '
      b += 1
    if int(num) != 0 and int(num) <= len(linhas):
      for l in range(len(linhas)):
        if pivoAux2[0] == organizar([linhas[l]])[0]:
          index = linhas.index(linhas[l])
          linhas.pop(l)
          linhas.append(atividade + '\n')
          break
      todo = open(TODO_FILE, 'w')
      for i in linhas:
        todo.write(i)
      todo.close()

def processarComandos(comandos) :

  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    itemParaAdicionar = organizar([' '.join(comandos)])[0]
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade

  elif comandos[1] == LISTAR:
    listar()
    return    

  elif comandos[1] == REMOVER:
    comandos.pop(0)
    comandos.pop(0)
    remover()
    return    
  elif comandos[1] == FAZER:
    comandos.pop(0)
    comandos.pop(0)
    num = int(sys.argv[0])
    fazer(num)
    return

  elif comandos[1] == PRIORIZAR:
    comandos.pop(0)
    comandos.pop(0)
    priorizar(comandos[0], comandos[1])
    return    

  else :
    print("Comando inválido.")
    
  
# sys.argv é uma lista de strings onde o primeiro elemento é o nome do programa
# invocado a partir da linha de comando e os elementos restantes são tudo que
# foi fornecido em sequência. Por exemplo, se o programa foi invocado como
#
# python3 agenda.py a Mudar de nome.
#
# sys.argv terá como conteúdo
#
# ['agenda.py', 'a', 'Mudar', 'de', 'nome']
processarComandos(sys.argv)
