#listar
import os

def listar():

    os.system("cls")

    try:

        #abre arquivo

        WHIT=open("arquivo.txt","r")

        pessoas=WHIT.readlines()

        printar=""

        #prepara uma mensagem com todos os nomes cadastrados
        
        for pessoa in pessoas:

            pessoa=pessoa.split("\n")
        
            printar=f"{printar}\n{pessoa[0]}"


    except:

        #exibe a mensagem quando o arquivo não existe ou se estiver vazio

        WHIT=open("arquivo.txt","a")
        
        printar="Arquivo vaio"

    
    print(printar)

    print("\n"*5)

    os.system("pause")


