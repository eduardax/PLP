#include <iostream>
#include <string.h>
#include <stdlib.h>

typedef struct{
char name[60], curso[20], cpf[14], rg[20], adress[200], hora_entrada[5], hora_saida[5], phone[12];
int id; //id - matricula
} aluno;
int op, x, op2, i_op2;     
                        
aluno estagiario[10];

using namespace std;

int main(){
	int indice = 0;
	
	cout << "\t\t\tTraineeTec\n\n";
		do{
			cout<<"\n\t\t\tMENU\n";
			cout<<"\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Exit\n";
			cout<<"Digite sua opção:\n";
			cin >> op;
				
			switch(op){
				case 1: 
						cout <<"\n\t\tCADASTRO\n";
						cout <<"\nNome:";
						fflush(stdin);
						cin >> estagiario[indice].name;
						cout <<"\nCPF:";
						fflush(stdin);
						cin >> estagiario[indice].cpf;
						cout <<"\nCurso:";
						fflush(stdin);
						cin >> estagiario[indice].curso;
						cout <<"\nRg:";
						fflush(stdin);
						cin >> estagiario[indice].rg;
						cout <<"\nEndereco:";
						fflush(stdin);
						cin >> estagiario[indice].adress;
						cout <<"\nHora de Entrada:";
						fflush(stdin);
						cin >> estagiario[indice].hora_entrada;
						cout <<"\nHora de Saída:";
						fflush(stdin);
						cin >> estagiario[indice].hora_saida;
						cout <<"\nCelular:";
						fflush(stdin);
						cin >> estagiario[indice].phone;
						cout <<"\nMatricula:";
						fflush(stdin);
						cin >> estagiario[indice].id;
							indice++;
					break;
					
				case 2:
						cout <<"\n\t\tEstagiarios Cadastrados\n";
							for(x=0;x<indice;x++){
								cout <<"\nNome: " <<estagiario[x].name;
								cout<<"\nMatricula: "<< estagiario[x].id;
								cout<<"\n";
								}
								cout<<"\nDigite a matricula desejada:\n";
								cin>> op2;
									for(x=0;x<indice;x++){
										if(estagiario[x].id==op2){
											i_op2=x;
											break;
										}
									}
									cout<<"\nEstagiario Encontrado:\n";
									cout<<"Nome: \n" <<estagiario[x].name;
									cout<<"Cpf: \n" <<estagiario[x].cpf;
									cout<<"Rg: \n" <<estagiario[x].rg;
									cout<<"Curso: \n" <<estagiario[x].curso;
									cout<<"Endereco: \n" <<estagiario[x].adress;
									cout<<"Hora de Entrada: \n" <<estagiario[x].hora_entrada;
									cout<<"Hora de Saida: \n" <<estagiario[x].hora_saida;
									cout<<"Celular: \n" <<estagiario[x].phone;
					break;
					
				case 3:
						cout<<"\nDigite a matricula desejada:\n";
						cin>> op2;
						for(x=0;x<indice;x++){
							if(estagiario[x].id==op2){
								i_op2=x;
								break;
							}
						}
						cout<<"\nNome:";
						fflush(stdin);
						cin>> estagiario[i_op2].name;
						cout<<"\nCPF:";
						fflush(stdin);
						cin>> estagiario[i_op2].cpf;
						cout<<"\nCurso:";
						fflush(stdin);
						cin>> estagiario[i_op2].curso;
						cout<<"\nRg:";
						fflush(stdin);
						cin>> estagiario[i_op2].rg;
						cout<<"\nEndereco:";
						fflush(stdin);
						cin>> estagiario[i_op2].adress;
						cout<<"\nHora de Entrada:";
						fflush(stdin);
						cin>> estagiario[i_op2].hora_entrada;
						cout<<"\nHora de Saída:";
						fflush(stdin);
						cin>> estagiario[i_op2].hora_saida;
						cout<<"\nCelular:";
						fflush(stdin);
						cin>> estagiario[i_op2].phone;
					break;
		
				case 4: 
				/*DELETE???????*/
					break;
			default: 0;
	}
		} while(op != 5);
		
	return 0;
}
