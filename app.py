# calculadora_imc.py
# Arquivo principal da calculadora de IMC com nome, idade, sexo e dicas profissionais
# Versão 2.8 - Totalmente comentada linha por linha sem exceção

# Importa o módulo os para manipular o sistema operacional
import os

# Importa o módulo datetime para trabalhar com data e hora
from datetime import datetime

# Importa o módulo json para salvar e carregar dados
import json

# Define o nome do arquivo onde o histórico será salvo
ARQUIVO_HISTORICO = "historico_imc.json"

# Define a função para limpar a tela do terminal
def limpar_tela():
    # Executa o comando de limpar tela de acordo com o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para obter um número float positivo do usuário
def obter_float_positivo(mensagem):
    # Inicia um loop infinito até o usuário digitar um valor válido
    while True:
        try:
            # Solicita a entrada do usuário e converte para float
            valor = float(input(mensagem))
            # Verifica se o valor digitado é maior que zero
            if valor <= 0:
                # Exibe mensagem de erro caso o valor seja inválido
                print("Erro: O valor deve ser maior que zero.")
                # Volta para o início do loop
                continue
            # Retorna o valor válido
            return valor
        # Captura erro caso o usuário digite algo que não seja número
        except ValueError:
            # Exibe mensagem de erro
            print("Erro: Por favor, digite um número válido.")

# Função para obter a idade do usuário
def obter_idade():
    # Inicia loop infinito até receber idade válida
    while True:
        try:
            # Solicita a idade e converte para número inteiro
            idade = int(input("Digite sua idade (anos): "))
            # Verifica se a idade está dentro de uma faixa razoável
            if 10 <= idade <= 120:
                # Retorna a idade válida
                return idade
            # Exibe erro caso idade esteja fora da faixa
            print("Erro: Idade deve estar entre 10 e 120 anos.")
        # Captura erro caso não seja digitado um número
        except ValueError:
            # Exibe mensagem de erro
            print("Erro: Por favor, digite um número inteiro válido.")

# Função para obter o sexo do usuário
def obter_sexo():
    # Inicia loop até receber entrada válida
    while True:
        # Solicita o sexo e remove espaços extras e converte para maiúsculo
        sexo = input("Digite seu sexo (M/F): ").strip().upper()
        # Verifica se a entrada é M ou F
        if sexo in ['M', 'F']:
            # Retorna o sexo
            return sexo
        # Exibe erro caso entrada seja inválida
        print("Erro: Digite 'M' para Masculino ou 'F' para Feminino.")

# Função para obter o nome do usuário
def obter_nome():
    # Inicia loop até nome válido
    while True:
        # Solicita o nome do usuário
        nome = input("Digite seu nome: ").strip()
        # Verifica se o nome não está vazio
        if nome:
            # Retorna o nome
            return nome
        # Exibe erro caso nome esteja vazio
        print("Erro: Por favor, digite seu nome.")

# Função que calcula o IMC
def calcular_imc(peso, altura_m):
    # Calcula o IMC usando a fórmula peso dividido pela altura ao quadrado
    imc = peso / (altura_m ** 2)
    # Arredonda o resultado para duas casas decimais
    return round(imc, 2)

# Função que define categoria do IMC e dicas profissionais
def obter_categoria_e_dicas(imc):
    # Verifica a faixa do IMC e define categoria
    if imc < 16.0:
        # Define dados para magreza grave
        categoria = "Magreza grave"
        cor = "\033[31m"
        mensagem = "Situação crítica."
        dica = "Consulte um médico urgentemente para avaliação completa."
    elif imc < 17.0:
        # Define dados para magreza moderada
        categoria = "Magreza moderada"
        cor = "\033[33m"
        mensagem = "Abaixo do peso ideal."
        dica = "Consulte um nutricionista para plano de ganho de peso saudável."
    elif imc < 18.5:
        # Define dados para magreza leve
        categoria = "Magreza leve"
        cor = "\033[36m"
        mensagem = "Abaixo do peso ideal."
        dica = "Aumente a ingestão calórica com alimentos nutritivos."
    elif imc < 25.0:
        # Define dados para peso normal
        categoria = "Peso normal"
        cor = "\033[32m"
        mensagem = "Peso dentro da faixa considerada saudável."
        dica = "Mantenha uma alimentação equilibrada e pratique atividade física regular."
    elif imc < 30.0:
        # Define dados para sobrepeso
        categoria = "Sobrepeso"
        cor = "\033[33m"
        mensagem = "Acima do peso ideal."
        dica = "Adote dieta equilibrada e aumente a atividade física diária."
    elif imc < 35.0:
        # Define dados para obesidade grau I
        categoria = "Obesidade grau I"
        cor = "\033[31m"
        mensagem = "Obesidade grau I."
        dica = "Procure orientação médica e nutricional para redução gradual de peso."
    elif imc < 40.0:
        # Define dados para obesidade grau II
        categoria = "Obesidade grau II"
        cor = "\033[31m"
        mensagem = "Obesidade grau II."
        dica = "Avaliação médica é altamente recomendada."
    else:
        # Define dados para obesidade grau III
        categoria = "Obesidade grau III"
        cor = "\033[31m"
        mensagem = "Obesidade grau III (mórbida)."
        dica = "Consulte imediatamente uma equipe multidisciplinar de saúde."
    
    # Retorna os valores de categoria, cor, mensagem e dica
    return categoria, cor, mensagem, dica

# Função principal que realiza o cálculo completo
def calcular_imc_principal():
    # Limpa a tela antes de iniciar o cálculo
    limpar_tela()
    
    # Exibe cabeçalho da aplicação
    print("=" * 70)
    print("          CALCULADORA DE IMC - PROFISSIONAL")
    print("=" * 70)
    print()
    
    # Coleta o nome do usuário
    nome = obter_nome()
    
    # Coleta a idade do usuário
    idade = obter_idade()
    
    # Coleta o sexo do usuário
    sexo = obter_sexo()
    
    # Coleta o peso do usuário
    peso = obter_float_positivo("Digite seu peso (kg): ")
    
    # Coleta a altura do usuário em metros
    altura_m = obter_float_positivo("Digite sua altura em METROS (ex: 1.75): ")
    
    # Calcula o IMC
    imc = calcular_imc(peso, altura_m)
    
    # Obtém categoria e dicas
    categoria, cor, mensagem, dica = obter_categoria_e_dicas(imc)
    
    # Exibe os resultados completos
    print("\n" + "=" * 70)
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos | Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}")
    print(f"Seu IMC é: {cor}{imc}\033[0m")
    print(f"Categoria: {cor}{categoria}\033[0m")
    print("=" * 70)
    
    # Exibe mensagem sobre a categoria
    print(f"\n{mensagem}")
    
    # Exibe dica profissional
    print(f"\nDica profissional: {dica}")
    
    # Exibe alerta importante
    print("\nATENCAO: O IMC não diferencia massa muscular de gordura corporal.")

# Função principal que controla o fluxo do programa
def main():
    # Loop infinito que mantém o programa rodando até o usuário sair
    while True:
        # Limpa a tela no início de cada ciclo
        limpar_tela()
        
        # Exibe o menu principal
        print("=" * 70)
        print("               MENU PRINCIPAL - IMC")
        print("=" * 70)
        print("1. Calcular IMC")
        print("0. Sair")
        print("=" * 70)
        
        # Solicita a opção do usuário
        opcao = input("\nEscolha uma opção: ").strip()
        
        # Verifica se o usuário escolheu calcular IMC
        if opcao == "1":
            # Chama a função de cálculo
            calcular_imc_principal()
            # Aguarda o usuário pressionar ENTER
            input("\nPressione ENTER para continuar...")
        # Verifica se o usuário escolheu sair
        elif opcao == "0":
            # Exibe mensagem de encerramento
            print("\nPrograma encerrado. Cuide da sua saúde!")
            # Encerra o loop
            break
        else:
            # Exibe mensagem para opção inválida
            print("Opção inválida.")
            # Aguarda o usuário
            input("Pressione ENTER para continuar...")

# Ponto de entrada do programa Python
if __name__ == "__main__":
    # Inicia a execução do programa
    main()