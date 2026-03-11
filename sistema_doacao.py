#Importação das funções do arquivo "Functions_database"
from functions_databese import criar_tabelas , cadastrar_doador , buscar_doadores , deletar_doador

def menu():
    criar_tabelas()

    while True:
        print("  \n     SISTEMA DE DOAÇÃO DE SANGUE:  \n   ")
        print("1. Cadastrar e Iniciar Triagem")
        print("2. Ver Lista de Doadores Cadastrados")
        print("3. Excluir Cadastro de Doador")
        print("4. Sair")
        
        # O input precisa estar DENTRO do while para repetir sempre
        opcao = input('Selecione uma opção: ')


          #CADASTRO E CHECAGEM DE APTIDÃO
        if opcao == "1":
            nome = input('\nNome Completo: ')
            idade = int(input(" Idade: "))                     
            peso = int(input(f"Peso: ").isdigit())   
            tipo_sanguineo = input("Tipo Sanguíneo: ").upper()
            print("\n")


            if idade >= 16 and idade <= 69 and peso <= 50:
                status = "APTO"
                print(f'Parabéns,{nome}. Você passou na Pré Triagem, Aguarde a Triagem Clínica para seguir com o processo!')
            else:
                status = "INAPTO"
                print(f"Prezado,{nome}. Infelizmente você não passou no Exame de Aptidão e não poderá doar Sangue.")
        

            

if __name__ == "__main__":
    menu()