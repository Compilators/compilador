def analisador_lexico(codigo_fonte):
    tokens = []
    tabela_simbolos = {}
    pos = 0
    linha = 1
    length = len(codigo_fonte)

    while pos < length:
        while codigo_fonte[pos] in ' \t':
            pos += 1
        if codigo_fonte[pos] == '\n':
            pos += 1
            linha += 1
        elif codigo_fonte[pos] == '+':
            tokens.append(('MAIS', '+', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '-':
            tokens.append(('MENOS', '-', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '*':
            tokens.append(('VEZES', '*', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '/':
            tokens.append(('DIVIDE', '/', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '=':
            if pos + 1 < len(codigo_fonte) and codigo_fonte[pos + 1] == '=':
                tokens.append(('IGUAL', '==', f'linha: {linha}'))
                pos += 2
            else:
                tokens.append(('ATRIBUICAO', '=', f'linha: {linha}'))
                pos += 1
        elif codigo_fonte[pos] == '!':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('DIFERENTE', '!=', f'linha: {linha}'))
                pos += 2
            else:
                print(f"Erro: Caractere inesperado '{codigo_fonte[pos]}' na posicao {pos+1}")
                pos += 1
        elif codigo_fonte[pos] == '>':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MAIOR_IGUAL', '>=', f'linha: {linha}'))
                pos += 2
            else:
                tokens.append(('MAIOR', '>', f'linha: {linha}'))
                pos += 1
        elif codigo_fonte[pos] == '<':
            if pos + 1 < length and codigo_fonte[pos + 1] == '=':
                tokens.append(('MENOR_IGUAL', '<=', f'linha: {linha}'))
                pos += 2
            else:
                tokens.append(('MENOR', '<', f'linha: {linha}'))
                pos += 1
        elif codigo_fonte[pos] == '(':
            tokens.append(('ABRE_PARENTESE', '(', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == ')':
            tokens.append(('FECHA_PARENTESE', ')', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == ',':
            tokens.append(('VIRGULA', ',', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == ':':
            tokens.append(('DOIS_PONTOS', ':', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '{':
            tokens.append(('ABRE_CHAVE', '{', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '}':
            tokens.append(('FECHA_CHAVE', '}', f'linha: {linha}'))
            pos += 1
        elif codigo_fonte[pos] == '"':
            inicio = pos
            pos += 1
            while pos < length and codigo_fonte[pos] != '"':
                pos += 1
            if pos < length and codigo_fonte[pos] == '"':
                tokens.append(('STRING', codigo_fonte[inicio + 1:pos], f'linha: {linha}'))
                pos += 1
            else:
                print(f"Erro: String nao terminada, começando na posicao {inicio+1}")
        elif codigo_fonte[pos].isalpha() or codigo_fonte[pos] == '_':
            inicio = pos
            pos += 1
            while pos < length and (codigo_fonte[pos].isalnum() or codigo_fonte[pos] == '_'):
                pos += 1
            palavra = codigo_fonte[inicio:pos]

            if palavra == 'verdadeiro' or palavra == 'falso':
                tipo = 'BOOLEANO'
            elif palavra == 'funcao':
                tipo = 'FUNCAO'
            elif palavra == 'se':
                tipo = 'SE'
            elif palavra == 'senao':
                tipo = 'SENAO'
            elif palavra == 'enquanto':
                tipo = 'ENQUANTO'
            elif palavra == 'interromper':
                tipo = 'INTERROMPER'
            elif palavra == 'continuar':
                tipo = 'CONTINUAR'
            elif palavra == 'imprimir':
                tipo = 'IMPRIMIR'
            elif palavra == 'inteiro':
                tipo = 'INTEIRO'
            elif palavra == 'booleano':
                tipo = 'BOOLEANO'
            elif palavra == 'vazio':
                tipo = 'VAZIO'
            elif palavra == 'retornar':
                tipo = 'RETORNAR'
            else:
                tipo = 'ID'

            palavra = codigo_fonte[inicio:pos]

            if palavra in tabela_simbolos:
                tokens.append((tabela_simbolos[palavra]['TIPO'], palavra, f'linha: {linha}'))
            else:
                valor = None
                lexema = None
                posicaoValor = pos
                posicaoFinal = pos
                while posicaoValor < length and codigo_fonte[pos] in ' \t':
                    posicaoValor += 1
                    if codigo_fonte[posicaoValor] == '=':
                        posicaoValor += 1
                        while posicaoValor < length and codigo_fonte[posicaoValor] in ' \t':
                            posicaoValor += 1
                            if codigo_fonte[posicaoValor].isdigit():
                                posicaoFinal = posicaoValor
                                while codigo_fonte[posicaoFinal] != '\n':
                                    posicaoFinal += 1
                                valor = codigo_fonte[posicaoValor:posicaoFinal]
                                lexema = 'NUMERO'
                                posicaoValor = 0
                                break
                            elif codigo_fonte[posicaoValor].isalpha():
                                posicaoFinal = posicaoValor
                                while codigo_fonte[posicaoFinal] != '\n':
                                    posicaoFinal += 1
                                if codigo_fonte[posicaoValor:posicaoFinal] == 'verdadeiro' or codigo_fonte[posicaoValor:posicaoFinal] == 'falso':
                                    lexema = 'BOOLEANO'
                                else:
                                    lexema = 'STRING'
                                valor = codigo_fonte[posicaoValor:posicaoFinal]
                                posicaoValor = 0
                                break
                            elif codigo_fonte[posicaoValor] == '"':
                                posicaoFinal = posicaoValor
                                posicaoValor += 1
                                while codigo_fonte[posicaoFinal] != '\n':
                                    posicaoFinal += 1
                                valor = codigo_fonte[posicaoValor-1:posicaoFinal]
                                posicaoValor = 0
                                lexema = 'STRING'
                                break
                            # elif codigo_fonte[posicaoValor] == '+' or codigo_fonte[posicaoValor] == '-' or codigo_fonte[posicaoValor] == '*' or codigo_fonte[posicaoValor] == '/':
                            #     posicaoValor += 1
                            #     while posicaoValor < length and codigo_fonte[posicaoValor] != '\n':
                            #         posicaoValor += 1
                            #     valor = codigo_fonte[posicaoValor:posicaoFinal]
                            #     posicaoValor = 0
                            #     break
                        break

                if tipo == 'ID':
                    tabela_simbolos[palavra] = {'TIPO': tipo, 'VALOR': valor, 'LEXEMA': lexema}
                tokens.append((tipo, palavra, f'linha: {linha}'))
        elif codigo_fonte[pos].isdigit():
            inicio = pos
            while pos < length and codigo_fonte[pos].isdigit():
                pos += 1
            tokens.append(('NUMERO', int(codigo_fonte[inicio:pos]), f'linha: {linha}'))
        else:
            raise Exception(f"Erro: Caractere invalido '{codigo_fonte[pos]}' na posicao {pos+1}")
    
    with open("tabela_simbolos.txt", 'w') as tabela_file:
        for palavra, atributos in tabela_simbolos.items():
            tabela_file.write(f"{palavra}: {atributos}\n")

    return tokens