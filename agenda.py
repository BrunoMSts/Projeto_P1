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

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)
  

# Adiciona um compromisso aa agenda. Um compromisso tem no minimo
# uma descrição. Adicionalmente, pode ter, em caráter opcional, uma
# data (formato DDMMAAAA), um horário (formato HHMM), uma prioridade de A a Z, 
# um contexto onde a atividade será realizada (precedido pelo caractere
# '@') e um projeto do qual faz parte (precedido pelo caractere '+'). Esses
# itens opcionais são os elementos da tupla "extras", o segundo parâmetro da
# função.
#
# extras ~ (data, hora, prioridade, contexto, projeto)
#
# Qualquer elemento da tupla que contenha um string vazio ('') não
# deve ser levado em consideração. 

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
  if len(pri) == 3 and pri[0] == '(' and 'a' <= pri[1] <= 'z' or 'A' <= pri[1] <= 'Z' and pri[2] == ')':
    return True
  else:
    return False


#FEITO------------------------------------
def horaValida(horaMin):
  if len(horaMin) == 4 and '0' <= horaMin[0] <= '2' and '0' <= horaMin[1] <= '3' and '0' <= horaMin[2] <= '5' and '0' <= horaMin[3] <= '9' and soDigitos(horaMin):
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


# Dadas as linhas de texto obtidas a partir do arquivo texto todo.txt, devolve
# uma lista de tuplas contendo os pedaços de cada linha, conforme o seguinte
# formato:
#
# (descrição, prioridade, (data, hora, contexto, projeto))
#
# É importante lembrar que linhas do arquivo todo.txt devem estar organizadas de acordo com o
# seguinte formato:
#
# DDMMAAAA HHMM (P) DESC @CONTEXT +PROJ
#
# Todos os itens menos DESC são opcionais. Se qualquer um deles estiver fora do formato, por exemplo,
# data que não tem todos os componentes ou prioridade com mais de um caractere (além dos parênteses),
# tudo que vier depois será considerado parte da descrição.  

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

# Datas e horas são armazenadas nos formatos DDMMAAAA e HHMM, mas são exibidas
# como se espera (com os separadores apropridados). 
#
# Uma extensão possível é listar com base em diversos critérios: (i) atividades com certa prioridade;
# (ii) atividades a ser realizadas em certo contexto; (iii) atividades associadas com
# determinado projeto; (vi) atividades de determinado dia (data específica, hoje ou amanhã). Isso não
# é uma das tarefas básicas do projeto, porém. 
def listar():

  ################ COMPLETAR
  return 

def ordenarPorDataHora(itens):

  ################ COMPLETAR

  return itens
   
def ordenarPorPrioridade(itens):

  ################ COMPLETAR

  return itens

def fazer(num):

  ################ COMPLETAR

  return 

def remover():

  ################ COMPLETAR

  return

# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'. 
def priorizar(num, prioridade):

  ################ COMPLETAR

  return 



# Esta função processa os comandos e informações passados através da linha de comando e identifica
# que função do programa deve ser invocada. Por exemplo, se o comando 'adicionar' foi usado,
# isso significa que a função adicionar() deve ser invocada para registrar a nova atividade.
# O bloco principal fica responsável também por tirar espaços em branco no início e fim dos strings
# usando o método strip(). Além disso, realiza a validação de horas, datas, prioridades, contextos e
# projetos. 
def processarComandos(comandos) :

  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    itemParaAdicionar = organizar([' '.join(comandos)])[0]
    # itemParaAdicionar = (descricao, (prioridade, data, hora, contexto, projeto))
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade

  elif comandos[1] == LISTAR:
    comandos.pop(0)
    comandos.pop(0)
    return    
    ################ COMPLETAR

  elif comandos[1] == REMOVER:
    return    

    ################ COMPLETAR    

  elif comandos[1] == FAZER:
    return

    ################ COMPLETAR

  elif comandos[1] == PRIORIZAR:
    return    

    ################ COMPLETAR

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
