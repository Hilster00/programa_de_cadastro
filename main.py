#main
import os
from cadastrar import cadastar
from listar import listar

while True:
    os.system("cls")
    print("(1) Cadastrar usuario")
    print("\n")
    print("(2) Vizualiar usuarios.")
    print("\n")
    print("'sair' para sair")
    try:

        #evita crashar quando usa ^c
         
        opcao=""

        opcao=(input("\n\n\n\n\n\n\nDigite a opcao desejada:"))

        opcao=int(opcao)

        if opcao == 1:

            cadastar()

        if opcao == 2:

            listar()

        
    except:

        os.system("cls")
            

        if opcao.lower() == "sair":

            break

        else:

            print(f"{opcao} invalida","\n"*23)

            os.system("pause")


