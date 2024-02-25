def analisador_lexico(codigo_fonte):
    tokens = []
    tabela_simbolos = {}
    pos = 0
    linha = 1
    length = len(codigo_fonte)

    def armazenaValor(palavra):
        posicaoInicialValor = codigo_fonte.rfind(palavra)
        posicao = codigo_fonte.rfind(palavra, codigo_fonte.find(palavra), posicaoInicialValor - (len(palavra) + 1)) 
        if posicaoInicialValor != -1: 
            posicaoInicialValor += len(palavra) 
            while posicaoInicialValor < len(codigo_fonte) and codigo_fonte[posicaoInicialValor] in ' \t':
                posicaoInicialValor += 1
                posicao -= 1 
                if codigo_fonte[posicaoInicialValor] == '=' and codigo_fonte[posicaoInicialValor + 1] != '=':
                    posicaoInicialValor += 1
                    while posicaoInicialValor < len(codigo_fonte) and codigo_fonte[posicaoInicialValor] in ' \t':
                        posicaoInicialValor += 1 
                        if codigo_fonte[posicaoInicialValor].isdigit():
                            posicaoFinalValor = posicaoInicialValor
                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor].isdigit():
                                posicaoFinalValor += 1
                            return codigo_fonte[posicaoInicialValor:posicaoFinalValor]
                        elif codigo_fonte[posicaoInicialValor] == '"':
                            posicaoFinalValor = posicaoInicialValor + 1
                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] != '"':
                                posicaoFinalValor += 1
                            if posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] == '"':
                                return codigo_fonte[posicaoInicialValor:posicaoFinalValor + 1]  
                        elif codigo_fonte[posicaoInicialValor].isalpha():
                            posicaoFinalValor = posicaoInicialValor
                            while posicaoFinalValor < len(codigo_fonte) and (codigo_fonte[posicaoFinalValor].isalnum() or codigo_fonte[posicaoFinalValor] == '_'):
                                posicaoFinalValor += 1
                            if codigo_fonte[posicaoInicialValor:posicaoFinalValor] == 'verdadeiro' or codigo_fonte[posicaoInicialValor:posicaoFinalValor] == 'falso':
                                return codigo_fonte[posicaoInicialValor:posicaoFinalValor]
                        elif codigo_fonte[posicaoInicialValor] in ('+', '-', '*', '/'):
                            posicaoFinalValor = posicaoInicialValor + 1
                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] in ('+', '-', '*', '/', ' '):
                                posicaoFinalValor += 1
                            return codigo_fonte[posicaoInicialValor:posicaoFinalValor]
                        posicaoInicialValor += 1
                else:
                    posicao += len(palavra) + 2
                    while (codigo_fonte[posicao] == "=" or codigo_fonte[posicao] == "+" or codigo_fonte[posicao] == '"') and codigo_fonte[posicao + 1] == "=":
                        posicao = codigo_fonte.rfind(palavra, codigo_fonte.find(palavra), posicao - (len(palavra) - 1))
                        posicao += len(palavra) + 1
                        if codigo_fonte[posicao] == '"':
                            posicao = codigo_fonte.rfind(palavra, codigo_fonte.find(palavra), posicao - (len(palavra) - 1))
                            posicao += len(palavra) + 1
                            if codigo_fonte[posicao] == '<':
                                posicao = codigo_fonte.rfind(palavra, codigo_fonte.find(palavra), posicao - (len(palavra) - 1))
                                posicao += len(palavra) + 1
                        if posicao != -1:
                                if codigo_fonte[posicao] == '=' and codigo_fonte[posicao + 1] != '=':
                                    posicao += 1
                                    while posicao < len(codigo_fonte) and codigo_fonte[posicao] in ' \t':
                                        posicao += 1
                                        if codigo_fonte[posicao].isdigit():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor].isdigit():
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] == '"':
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] != '"':
                                                posicaoFinalValor += 1
                                            if posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] == '"':
                                                return codigo_fonte[posicao:posicaoFinalValor + 1]  
                                        elif codigo_fonte[posicao].isalpha():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and (codigo_fonte[posicaoFinalValor].isalnum() or codigo_fonte[posicaoFinalValor] == '_'):
                                                posicaoFinalValor += 1
                                            if codigo_fonte[posicao:posicaoFinalValor] == 'verdadeiro' or codigo_fonte[posicao:posicaoFinalValor] == 'falso':
                                                return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] in ('+', '-', '*', '/'):
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] in ('+', '-', '*', '/', ' '):
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        posicao += 1
                                elif codigo_fonte[posicao] == '+' and codigo_fonte[posicao + 1] == '=':
                                    posicao += 1
                                    while posicao < len(codigo_fonte) and codigo_fonte[posicao] in ' \t':
                                        posicao += 1
                                        if codigo_fonte[posicao].isdigit():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor].isdigit():
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] == '"':
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] != '"':
                                                posicaoFinalValor += 1
                                            if posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] == '"':
                                                return codigo_fonte[posicao:posicaoFinalValor + 1]  
                                        elif codigo_fonte[posicao].isalpha():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and (codigo_fonte[posicaoFinalValor].isalnum() or codigo_fonte[posicaoFinalValor] == '_'):
                                                posicaoFinalValor += 1
                                            if codigo_fonte[posicao:posicaoFinalValor] == 'verdadeiro' or codigo_fonte[posicao:posicaoFinalValor] == 'falso':
                                                return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] in ('+', '-', '*', '/'):
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] in ('+', '-', '*', '/', ' '):
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        posicao += 1
                                elif codigo_fonte[posicao] == '-' and codigo_fonte[posicao + 1] == '=':
                                    posicao += 1
                                    while posicao < len(codigo_fonte) and codigo_fonte[posicao] in ' \t':
                                        posicao += 1
                                        if codigo_fonte[posicao].isdigit():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor].isdigit():
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] == '"':
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] != '"':
                                                posicaoFinalValor += 1
                                            if posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] == '"':
                                                return codigo_fonte[posicao:posicaoFinalValor + 1]  
                                        elif codigo_fonte[posicao].isalpha():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and (codigo_fonte[posicaoFinalValor].isalnum() or codigo_fonte[posicaoFinalValor] == '_'):
                                                posicaoFinalValor += 1
                                            if codigo_fonte[posicao:posicaoFinalValor] == 'verdadeiro' or codigo_fonte[posicao:posicaoFinalValor] == 'falso':
                                                return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] in ('+', '-', '*', '/'):
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] in ('+', '-', '*', '/', ' '):
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        posicao += 1
                                elif codigo_fonte[posicao] == '*' and codigo_fonte[posicao + 1] == '=':
                                    posicao += 1
                                    while posicao < len(codigo_fonte) and codigo_fonte[posicao] in ' \t':
                                        posicao += 1
                                        if codigo_fonte[posicao].isdigit():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor].isdigit():
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] == '"':
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] != '"':
                                                posicaoFinalValor += 1
                                            if posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] == '"':
                                                return codigo_fonte[posicao:posicaoFinalValor + 1]  
                                        elif codigo_fonte[posicao].isalpha():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and (codigo_fonte[posicaoFinalValor].isalnum() or codigo_fonte[posicaoFinalValor] == '_'):
                                                posicaoFinalValor += 1
                                            if codigo_fonte[posicao:posicaoFinalValor] == 'verdadeiro' or codigo_fonte[posicao:posicaoFinalValor] == 'falso':
                                                return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] in ('+', '-', '*', '/'):
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] in ('+', '-', '*', '/', ' '):
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        posicao += 1
                    if posicao != -1:
                                if codigo_fonte[posicao] == '=' and  codigo_fonte[posicao + 1] != '=':
                                    posicao += 1
                                    while posicao < len(codigo_fonte) and codigo_fonte[posicao] in ' \t':
                                        posicao += 1
                                        if codigo_fonte[posicao].isdigit():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor].isdigit():
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] == '"':
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] != '"':
                                                posicaoFinalValor += 1
                                            if posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] == '"':
                                                return codigo_fonte[posicao:posicaoFinalValor + 1]  
                                        elif codigo_fonte[posicao].isalpha():
                                            posicaoFinalValor = posicao
                                            while posicaoFinalValor < len(codigo_fonte) and (codigo_fonte[posicaoFinalValor].isalnum() or codigo_fonte[posicaoFinalValor] == '_'):
                                                posicaoFinalValor += 1
                                            if codigo_fonte[posicao:posicaoFinalValor] == 'verdadeiro' or codigo_fonte[posicao:posicaoFinalValor] == 'falso':
                                                return codigo_fonte[posicao:posicaoFinalValor]
                                        elif codigo_fonte[posicao] in ('+', '-', '*', '/'):
                                            posicaoFinalValor = posicao + 1
                                            while posicaoFinalValor < len(codigo_fonte) and codigo_fonte[posicaoFinalValor] in ('+', '-', '*', '/', ' '):
                                                posicaoFinalValor += 1
                                            return codigo_fonte[posicao:posicaoFinalValor]
                                        posicao += 1

        return None


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
                tabela_simbolos[palavra] = {'TIPO': tipo, 'VALOR': armazenaValor(palavra)}
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
                            elif codigo_fonte[posicaoValor] == '+' or codigo_fonte[posicaoValor] == '-' or codigo_fonte[posicaoValor] == '*' or codigo_fonte[posicaoValor] == '/':
                                posicaoValor += 1
                                while posicaoValor < length and codigo_fonte[posicaoValor] != '\n':
                                    posicaoValor += 1
                                valor = codigo_fonte[posicaoValor:posicaoFinal]
                                posicaoValor = 0
                                lexema = 'NUMERO'
                                break
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
    
    def verificaLexema(palavra):
        if palavra.isnumeric():
            return 'NUMERO'
        elif palavra == 'verdadeiro' or palavra == 'falso':
            return 'BOOLEANO'
        elif palavra[0] == '"' and palavra[-1] == '"':
            return 'STRING'
        else:
            return 'None'
        
    for palavra, atributos in tabela_simbolos.items():
        if atributos['VALOR'] != None:
            tabela_simbolos[palavra]['LEXEMA'] = verificaLexema(atributos['VALOR'])

    with open("tabela_simbolos.txt", 'w') as tabela_file:
        for palavra, atributos in tabela_simbolos.items():
            tabela_file.write(f"{palavra}: {atributos}\n")

    return tokens
