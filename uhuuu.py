import os
PATH = 'estagiarios/'

def create(nome, cpf, curso, rg, endereco, hora_entrada, hora_saida, celular, matricula):
  pasta = os.listdir(PATH)
  if pasta.count(matricula+'.txt')==0:
      estagiario=open(PATH+matricula+'.txt', 'w', encoding="utf8" )
      estagiario.write('Nome: {}\n'.format(nome))
      estagiario.write("Matrícula: {}\n".format(matricula))
      estagiario.write("CPF: {}\n".format(cpf))
      estagiario.write("Curso: {}\n".format(curso))
      estagiario.write("RG: {}\n".format(rg))
      estagiario.write("Endereço: {}\n".format(endereco))
      estagiario.write("Hora de Entrada: {}\n".format(hora_entrada))
      estagiario.write("Hora de Saída: {}\n".format(hora_saida))
      estagiario.write("Celular: {}\n".format(celular))
      estagiario.close()
  else:
      print ("Matrícula existente")

def read_all(matricula):
    pasta = os.listdir (PATH)
    if matricula + '.txt' in pasta:
        estagiario = open(PATH + matricula + '.txt', 'r', encoding="utf8")
        print(estagiario.read())

    else:
        print("Matrícula não existe")

def read_2():
    pasta = os.listdir(PATH)
    for i in pasta:
        estagiario = open(PATH + i, 'r', encoding="utf8")
        print(estagiario.readline() + estagiario.readline())



def update (nome, cpf, curso, rg, endereco, hora_entrada, hora_saida, celular, matricula):
        pasta = os.listdir(PATH)
        if pasta.count(matricula + '.txt') == 1:
            os.remove(PATH + matricula + '.txt')
            estagiario = open(PATH + matricula + '.txt', 'w', encoding="utf8")
            estagiario.write('Nome: {}\n'.format(nome))
            estagiario.write("Matrícula: {}\n".format(matricula))
            estagiario.write("CPF: {}\n".format(cpf))
            estagiario.write("Curso: {}\n".format(curso))
            estagiario.write("RG: {}\n".format(rg))
            estagiario.write("Endereco: {}\n".format(endereco))
            estagiario.write("Hora de Entrada: {}\n".format(hora_entrada))
            estagiario.write("Hora de Saida: {}\n".format(hora_saida))
            estagiario.write("Celular: {}\n".format(celular))
            estagiario.close()
        else:
            print("Matrícula inexistente")


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
      print ("\n\t\tESTAGIÁRIOS CADASTRADOS\n")
      read_2()
      matricula = input("Digite a matricula desejada:\n\n")
      read_all(matricula)
      print("\n")
  if op==3:
      print("\n\tATUALIZAÇÃO DO CADASTRO\n")
      matricula = input("Digite a matrícula desejada:\n")
      nome = input("Nome:\n")
      cpf = input("CPF:\n")
      curso = input("Curso:\n")
      rg = input("Rg:\n")
      endereco = input("Endereço:\n")
      hora_entrada = input("Hora de Entrada:\n")
      hora_saida = input("Hora de Saída:\n")
      celular = input("Celular:\n")
      matricula = input("Matrícula:\n")
      update(nome, cpf, curso, rg, endereco, hora_entrada, hora_saida, celular, matricula)
      print("\n\t\tCADASTRO ATUALIZADO \n")
      read_all(matricula)
      print("\n")
  if op==4:
    print("\n\t\tEXCLUSÃO DE ESTAGIÁRIOS\n")
    matricula = input("Digite a matrícula desejada:\n")
    print("Estagiário excluído")

    if matricula + '.txt' in os.listdir(PATH):
        os.remove(PATH + matricula + '.txt')
    else:
        print("Matrícula Inexistente")

#OBRIGADA MATEUS, MEU CONSAGRADO! (IMAGINA UM COALA E UM CORAÇÃO AZUL) <3
