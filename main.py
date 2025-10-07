from funcoes import *
import os

def main():
    while True:
        try:
            print("\n--- GERADOR DE RELATÓRIOS ---")
            print("1 - Relatório simples")
            print("2 - Relatório com título")
            print("3 - Relatório com título e rodapé")
            print("4 - Relatório com múltiplos parágrafos")
            print("5 - Relatório completo com metadados")
            print("0 - Sair")
                
            escolha = input("Escolha uma opção: ")

            match escolha:
                case "1":
                    relatorio_1()
                    os.system ("pause")
                    os.system ("cls")

                case "2":
                    relatorio_2()

                case "3":
                    relatorio_3()

                case "4":
                    relatorio_4()

                case "5":
                    relatorio_5()
                    
                case "0":
                    print("Saindo...")
                    break

                case _:
                    print("Opção inválida! Tente novamente.")

        except:
            print(f"Ocorreu um erro! Tente Novamente")


if __name__ == "__main__":
    main()
