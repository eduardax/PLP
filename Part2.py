estagiarios = []

def create(nome, cpf, curso, rg, endereco, hora_entrada, hora_saida, celular, matricula):
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

print "\t\t\tTreinee TEC\n"

print "1-Create\n2-Read\n3-Upload\n4-Delete\n5-Exit\n"
op = input("Digite sua opcao:\n")

if op==1:
    print "\t\tCADASTRO\n"
    name = input("Nome:\n")
    cpf = input("CPF:\n")
    curso = input("Curso:\n")
    rg = input("Rg:\n")
    endereco = input("Endereco:\n")
    hora_entrada = input("Hora de Entrada:\n")
    hora_saida = input("Hora de Saída:\n")
    celular = input("Celular:\n")
    matricula = input("Matricula:\n")
    create (nome, cpf, curso, rg, endereco, hora_entrada, hora_saida, celular, matricula):
if op==2:
    print "\n\t\tEstagiarios Cadastrados\n"
    for i in estagiarios:
        for i in i.items():
            print ('Nome: {} : Matricula: {}'. format (nome), (matricula))
        print('\n')
    op2 = input("")
