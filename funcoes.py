from classes import *

def relatorio_1():
        a = Gerador_Relatorio()
        print("-- Relatório 1 --")
        print(a.gerar("Relatório de Vendas de Carro"))

def relatorio_2():
        a = Gerador_Relatorio()
        print("-- Relatório 2 --")
        print(a.gerar("Relatório de Vendas de Carro", "Vendas totais de Carro - R$732.877"))

def relatorio_3():
        a = Gerador_Relatorio()
        print("-- Relatório 3 --")
        print(a.gerar("Relatório Financeiro", "Lucro Líquido - R$244.292,33", "Confidencial"))

def relatorio_4():
        a = Gerador_Relatorio()
        print("-- Relatório 4 --")
        print(a.gerar(
            "Relatório Semanal",
            "As vendas aumentaram em 20%",
            "O carro mais vendido foi o Lancer GT",
            "A expectativa da empresa é de crescimento de 6 em 6 meses"
        ))


def relatorio_5():
        a = Gerador_Relatorio()
        print("-- Relatório 5 --")
        print(a.gerar(
            "Relatório Mensal",
            "Resumo Geral do mês de Janeiro",
            "As metas da empresa foram alcançadas",
            metadados={"Autor": "Moisés Gabriel Tafarello", "Data": "07/02/2025", "Versão": "1.0"}
        ))
    
