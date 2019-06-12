TODO_FILE = 'todo.txt'

def prioridadeValida(pri):
  if len(pri) == 3 and pri[0] == '(' and 'a' <= pri[1] <= 'z' or 'A' <= pri[1] <= 'Z' and pri[2] == ')':
    return True
  else:
    return False


#FEITO------------------------------------
def horaValida(horaMin):
  if len(horaMin) == 4 and '0' <= horaMin[0] <= '2' and '0' <= horaMin[1] <= '3' and '0' <= horaMin[2] <= '5' and '0' <= horaMin[3] <= '9':
    return True
  else:
    return False

#FEITO--------------------------------------
def dataValida(data):
  if len(data) == 8:
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

#FEITO-----------------------------------------------
def organizar(linhas):
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
        if prioridadeValida(tokens[0]):
          pri = tokens.pop(0)
    elif horaValida(tokens[0]):
      hora = tokens.pop(0)
      if prioridadeValida(tokens[0]):
        pri = tokens.pop(0)
    elif prioridadeValida(tokens[0]):
      pri = tokens.pop(0)
    if projetoValido(tokens[-1]):
      projeto = tokens.pop()
      if contextoValido(tokens[-1]):
        contexto = tokens.pop()
    elif contextoValido(tokens[-1]):
      contexto = tokens.pop()
    for i in tokens:
      desc += i + ' '
    itens.append((desc, (data, hora, pri, contexto, projeto)))
  return itens

#print(organizar(['010325000 1030 (A) Bruno gostoso oiasd @contexto +projeto']))

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
          novaAtividade += descricao + ' '
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
itens = [('teste',('20112000','1030','(A)','@oiedsa', '+prsai'))]

print(adicionar('oi isso é um teste', itens))