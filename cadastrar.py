#cadastrar

import os

def cadastar():

    #criar arquivo caso nao exista

    os.system("cls") 

    WHIT=open("arquivo.txt","a")

    WHIT.close()



    while True:

        print("Digite 'sair' para sair\n")

        try:

            #evita crashar quando usa ^c

            pessoa=""

            pessoa=input("Digite o novo nome:")

            if pessoa.isnumeric() == True or pessoa == "":

                #redireciona para o except para exibir mensagem de erro 

                invalido=1/0

            if pessoa.upper() == "SAIR":

                break

            else:
                #adicionar usuario
                
                WHIT=open("arquivo.txt","a")

                pessoa=pessoa.title()

                WHIT.write(f"\n{pessoa}")

                os.system("cls")

                print(f"{pessoa} foram cadastradas com sucesso","\n"*23)

                os.system("pause")

                os.system("cls")

                WHIT.close()

            
        except :
            
            os.system("cls")

            print(f"Nome {pessoa} invalido") 
   
    








