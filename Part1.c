#include <stdio.h>
#include <string.h>
#include <locale.h>

typedef struct{
char name[60], curso[20], cpf[14], rg[20], adress[200], hora_entrada[5], hora_saida[5], phone[12];
int id; //id - matricula
} aluno;
int op, x, op2, i_op2;     
                        //\a - apito(efeito sonoro)
aluno estagiario[10];

void main(void){
	
	int indice = 0;
	
	printf("\t\t\tStartup Shit\n");
	do{
	printf("1-Create\n2-Read\n3-Update\n4-Delete\n5-Exit\n");
	printf("Digite sua opção:\n");
	scanf("%i", &op);
	switch(op){
		case 1: printf("\n\t\tCADASTRO\n");
				printf("Nome:\n");
				fflush(stdin);
				gets(estagiario[indice].name);
				printf("CPF:\n");
				fflush(stdin);
				gets(estagiario[indice].cpf);
				printf("Curso:\n");
				fflush(stdin);
				gets(estagiario[indice].curso);
				printf("Rg:\n");
				fflush(stdin);
				gets(estagiario[indice].rg);
				printf("Endereco:\n");
				fflush(stdin);
				gets(estagiario[indice].adress);
				printf("Hora de Entrada:\n");
				fflush(stdin);
				gets(estagiario[indice].hora_entrada);
				printf("Hora de Saída:\n");
				fflush(stdin);
				gets(estagiario[indice].hora_saida);
				printf("Celular:\n");
				fflush(stdin);
				gets(estagiario[indice].phone);
				printf("Matricula:\n");
				fflush(stdin);
				scanf("%i", &estagiario[indice].id);
					indice++;
			break;
		case 2: printf("\n\t\tEstagiarios Cadastrados\n");
				for(x=0;x<indice;x++){
				printf("Nome: %s\n", estagiario[x].name);
				printf("Matricula: %i\n", estagiario[x].id);
				}
				printf("Digite a matricula desejada:\n");
				scanf("%i", &op2);
					for(x=0;x<indice;x++){
						if(estagiario[x].id==op2){
							i_op2=x;
							break;
						}
					}
					printf("Estagiario Encontrado:");
					printf("Nome: %s\n", estagiario[x].name);
					printf("Cpf: %s\n", estagiario[x].cpf);
					printf("Rg: %s\n", estagiario[x].rg);
					printf("Curso: %s\n", estagiario[x].curso);
					printf("Endereco: %s\n", estagiario[x].adress);
					printf("Hora de Entrada: %s\n", estagiario[x].hora_entrada);
					printf("Hora de Saida: %s\n", estagiario[x].hora_saida);
					printf("Celular: %s\n", estagiario[x].phone);
			break;
		case 3: printf("Digite a matricula desejada:\n");
				scanf("%i", &op2);
				for(x=0;x<indice;x++){
				if(estagiario[x].id==op2){
					i_op2=x;
							break;}
							}
				printf("Nome:\n");
				fflush(stdin);
				gets(estagiario[i_op2].name);
				printf("CPF:\n");
				fflush(stdin);
				gets(estagiario[i_op2].cpf);
				printf("Curso:\n");
				fflush(stdin);
				gets(estagiario[i_op2].curso);
				printf("Rg:\n");
				fflush(stdin);
				gets(estagiario[i_op2].rg);
				printf("Endereco:\n");
				fflush(stdin);
				gets(estagiario[i_op2].adress);
				printf("Hora de Entrada:\n");
				fflush(stdin);
				gets(estagiario[i_op2].hora_entrada);
				printf("Hora de Saída:\n");
				fflush(stdin);
				gets(estagiario[i_op2].hora_saida);
				printf("Celular:\n");
				fflush(stdin);
				gets(estagiario[i_op2].phone);
			break;
		case 4: 
				/*DELETE???????*/
			break;
		default: 0;
	}
		}while(op!= 5);
	
}
