# calculadora_imc.py
# Arquivo principal da calculadora de IMC

# Importa o módulo necessário para manipular o sistema operacional
import os

# Define a função para limpar a tela do terminal
def limpar_tela():
    # Comando para limpar tela no Windows ou Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# Define a função principal de cálculo do IMC
def calcular_imc():
    # Chama a função para limpar a tela antes de iniciar
    limpar_tela()
    
    # Exibe o cabeçalho da aplicação
    print("=== CALCULADORA DE IMC - MÉDICA E TREINO ===\n")
    
    # Recebe o peso do usuário
    peso = float(input("Digite seu peso (kg): "))
    
    # Recebe a altura do usuário
    altura = float(input("Digite sua altura (metros): "))
    
    # Realiza o cálculo do IMC
    imc = peso / (altura ** 2)
    
    # Arredonda o IMC para duas casas decimais
    imc = round(imc, 2)
    
    # Inicia verificação da categoria do IMC
    if imc < 18.5:
        # Define categoria para baixo peso
        categoria = "Baixo peso"
        # Define cor ciano para o texto
        cor = "\033[36m"
        # Define mensagem para o usuário
        mensagem = "Você está abaixo do peso ideal. Consulte um médico ou nutricionista."
    
    # Verifica se está na faixa normal
    elif imc < 25:
        # Define categoria peso normal
        categoria = "Peso normal"
        # Define cor verde
        cor = "\033[32m"
        # Define mensagem positiva
        mensagem = "Parabéns! Seu peso está dentro da faixa considerada saudável."
    
    # Verifica se está em sobrepeso
    elif imc < 30:
        # Define categoria sobrepeso
        categoria = "Sobrepeso"
        # Define cor amarela
        cor = "\033[33m"
        # Define mensagem de alerta
        mensagem = "Cuidado. Recomenda-se acompanhamento nutricional e atividade física."
    
    # Caso contrário (obesidade)
    else:
        # Define categoria obesidade
        categoria = "Obesidade"
        # Define cor vermelha
        cor = "\033[31m"
        # Define mensagem de recomendação médica
        mensagem = "Procure um médico e nutricionista para avaliação detalhada."
    
    # Exibe separador visual
    print("\n" + "="*50)
    
    # Exibe o valor do IMC com cor
    print(f"Seu IMC é: {cor}{imc}\033[0m")
    
    # Exibe a categoria com cor
    print(f"Categoria: {cor}{categoria}\033[0m")
    
    # Exibe separador visual novamente
    print("="*50)
    
    # Exibe mensagem explicativa
    print(f"\n{mensagem}")
    
    # Exibe alerta para praticantes de treino
    print("\n⚠️  ATENÇÃO PARA ATLETAS E PRATICANTES DE MUSCULAÇÃO:")
    
    # Linha 1 do alerta
    print("O IMC não diferencia massa muscular de gordura.")
    
    # Linha 2 do alerta
    print("Pessoas muito musculosas podem ter IMC elevado, mas baixa gordura corporal.")
    
    # Linha 3 do alerta
    print("Considere também medir circunferência abdominal e percentual de gordura.")

# Ponto de entrada do programa
if __name__ == "__main__":
    # Inicia loop para múltiplos cálculos
    while True:
        # Executa o cálculo
        calcular_imc()
        
        # Pergunta se deseja continuar
        continuar = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
        
        # Verifica se deve encerrar
        if continuar != 's':
            # Mensagem de encerramento
            print("Programa encerrado. Cuide da sua saúde!")
            # Encerra o loop
            break