# Texto do arquivo
texto = """
variavel_inteira = 55
variavel_inteira = "teste"
variavel_booleana = verdadeiro


"""

# Palavra que você deseja encontrar
palavra = "variavel_inteira"

# Lista para armazenar as posições de todas as ocorrências da palavra
posicoes = 0

# Índice para rastrear a posição atual no texto
indice = 0

# Enquanto houver ocorrências da palavra no texto
while True:
    # Encontra a próxima ocorrência da palavra a partir da posição atual
    posicao = texto.find(palavra, indice)
    print(posicao)

    
    # Se não encontrar mais ocorrências, interrompe o loop
    if posicao == -1:
        break
    
    # Armazena a posição encontrada na lista de posições
    posicoes = posicao
    
    # Atualiza o índice para continuar a busca após a última ocorrência encontrada
    indice = posicao + len(palavra)

# Imprime as posições encontradas
print("Posições encontradas:", posicoes)
