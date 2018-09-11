estagiarios = []

def create(name, cpf, curso, rg, endereco, hora_entrada, hora_saida, celular, matricula):
    estagiarios.append({  #adiciona um coisa dentro do vetor matricula
        'nome' : nome,
        'cpf' : cpf,
        'curso' : curso,
        'rg' : rg,
        'endereco' : endereco,
        'hora_entrada':hora_entrada,
        'hora_saida':hora_saida,
        'celular':celular,
        'matricula' : matricula,
    })

def read_all(matricula):
    for i in estagiarios:
        if i['matricula']==matricula:
          print("Nome: {}".format(i['nome']))
          print("Matricula: {}".format(i['matricula']))
          print("CPF: {}".format(i['cpf']))
          print("Curso: {}".format(i['curso']))
          print("RG: {}".format(i['rg']))
          print("Endereco: {}".format(i['endereco']))
          print("Hora de Entrada: {}".format(i['hora_entrada']))
          print("Hora de Saida: {}".format(i['hora_saida']))
          print("Celular: {}".format(i['celular']))
      
def read_2():
  for i in estagiarios:
      print("Nome: {}".format(i['nome']))
      print("Matricula: {}".format(i['matricula']))

def read_3(matricula):
  for i in estagiarios:
    if i['matricula']==matricula:
      i['nome'] = input("Nome:\n")
      i['cpf'] = input("CPF:\n")
      i['curso'] = input("Curso:\n")
      i['rg'] = input("Rg:\n")
      i['endereco'] = input("Endereco:\n")
      i['hora_entrada'] = input("Hora de Entrada:\n")
      i['hora_saida'] = input("Hora de Saída:\n")
      i['celular'] = input("Celular:\n")

print ("\t\t\tTrainee TEC\n")
op = 0
while (op != 5):
  print ("\n\n\t\tMENU\n")
  print ("1-Create\n2-Read\n3-Upload\n4-Delete\n5-Exit\n")
  op = int (input("Digite sua opcao:\n"))

  if op==1:
      print ("\t\tCADASTRO\n")
      nome = input("Nome:\n")
      cpf = input("CPF:\n")
      curso = input("Curso:\n")
      rg = input("Rg:\n")
      endereco = input("Endereco:\n")
      hora_entrada = input("Hora de Entrada:\n")
      hora_saida = input("Hora de Saída:\n")
      celular = input("Celular:\n")
      matricula = input("Matricula:\n")
      create (nome, cpf, curso, rg, endereco, hora_entrada, hora_saida, celular, matricula)
  if op==2:
      print ("\n\t\tESTAGIARIOS CADASTRADOS\n")
      read_2()
      matricula = input("Digite a matricula desejada:\n")
      read_all(matricula)
      print("\n")
  if op==3:
      print("\n\tATUALIZAÇÃO DO CADASTRO\n")
      matricula = input("Digite a matricula desejada:\n")
      read_3(matricula)
      print("\n\t\tCADASTRO ATUALIZADO \n")
      read_all(matricula)
      print("\n")
  if op==4:
    print("\n\t\tEXCLUSÃO DE ESTAGIARIOS\n")
    matricula = input("Digite a matricula desejada:")
    estagiarios.pop()
