import sys
class Sintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.atual_token = None
        self.prox_token()

    def prox_token(self):
        try:
            self.atual_token = next(self.tokens)
        except StopIteration:
            self.atual_token = None
            
    def match(self, *tipo_token):
        while self.atual_token and self.atual_token[0] in ['DOIS_PONTOS', 'VIRGULA']:
            if self.atual_token[0] == 'VIRGULA':
                self.prox_token()
            else:
                self.prox_token()

        if self.atual_token and self.atual_token[0] in tipo_token:
            self.prox_token()
            return True
        elif self.atual_token and self.atual_token[0] == 'FECHA_PARENTESE':
            return True
        else:
            # print(f"Erro: Esperado {', '.join(tipo_token)}, mas encontrou {self.atual_token}")
            return False

    def programa(self):
        while self.atual_token:
            self.token()
            if self.atual_token is None:
                print("Execucao finalizada com sucesso.")
                break

    def token(self):
        print(self.atual_token)
        match self.atual_token[0]:
            case 'ID':
                self.chamada_funcao()
            case 'FUNCAO':
                self.declaracao_funcao()
            case 'SE':
                self.if_condicional()
            case 'ENQUANTO':
                self.enquanto_condicional()
            case 'IMPRIMIR':
                self.imprimir()
            case _:
                print(f"Erro: Expressao invalida. Encontrou {self.atual_token}")
                sys.exit(1)
    
    def parenteses_expressao(self):
        if not self.match('ABRE_PARENTESE'):
            raise Exception(f"Erro: Abre parentese nao encontrado, mas encontrado {self.atual_token}.")
        self.expressao()
        if not self.match('FECHA_PARENTESE'):
            raise Exception(f"Erro: Fecha parentese nao encontrado, mas encontrado {self.atual_token}.")
    
    def op_aditivo(self):
        while self.atual_token and self.atual_token[0] in ['MAIS', 'MENOS']:
            operador = self.atual_token[1]
            self.prox_token()
        return operador

    def expressao(self):
        self.termo()

        while self.atual_token and self.atual_token[0] in ['MAIOR', 'MENOR', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'IGUAL', 'DIFERENTE']:
            operador = self.atual_token[1]
            self.prox_token()
            self.termo()

    def termo(self):
        self.fator()

        while self.atual_token and self.atual_token[0] in ['MAIS', 'MENOS']:
            operador_aditivo = self.op_aditivo()
            self.fator()

    def fator(self):
        if self.atual_token and self.atual_token[0] == 'NUMERO':
            self.prox_token()
        elif self.atual_token and self.atual_token[0] == 'ID':
            self.prox_token()
            if self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
                self.lista_argumentos()
                self.match('FECHA_PARENTESE')
        elif self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
            self.parenteses_expressao()
        elif self.atual_token and self.atual_token[0] == 'BOOLEANO':
            self.prox_token()
        else:
            raise Exception(f"Erro: Fator invalido, encontrado {self.atual_token}.")
    
    def escopo(self):
        if not self.match('ABRE_CHAVE'):
            raise Exception(f"Erro: Abre chaves nao encontrado, mas encontrado {self.atual_token}.")
        while self.atual_token[0] != 'FECHA_CHAVE':
            if self.atual_token[0] == 'IMPRIMIR':
                self.imprimir()
            elif self.atual_token[0] == 'SE':
                self.if_condicional()
            elif self.atual_token[0] == 'ENQUANTO':
                self.enquanto_condicional()
            elif self.atual_token[0] == 'ID':
                self.chamada_funcao()
            if self.atual_token[0] == 'CONTINUAR':
                self.continue_condicional()
            elif self.atual_token[0] == 'INTERROMPER':
                self.break_condicional()
        if not self.match('FECHA_CHAVE'):
            raise Exception(f"Erro: Fecha chaves nao encontrado, mas encontrado {self.atual_token}.")
           
    def enquanto_condicional(self):
        if not self.match('ENQUANTO'):
            raise Exception(f"Erro: 'ENQUANTO' esperado, mas encontrado {self.atual_token}")
        self.parenteses_expressao()
        self.escopo()
        self.token()

    def imprimir(self):
        if self.match('IMPRIMIR'):
            self.match('ABRE_PARENTESE')
            while self.atual_token[0] in ['ID', 'STRING', 'NUMERO', 'BOOLEANO']:
                self.prox_token()
            if not self.match('FECHA_PARENTESE'):
                raise Exception(f"Erro: Fecha parentese nao encontrado, mas encontrado {self.atual_token}.")
        else:
            print("Erro: Esperado 'IMPRIMIR'")

    def declaracao(self):
        if self.match('INTEIRO', 'BOOLEANO', 'VAZIO'):
            self.tipo_declaracao()
        else:
            if self.match('ID'):
                self.atribuicao()

    def tipo_declaracao(self):
        if self.match('ID'):
            if self.match('ABRE_PARENTESE'):
                self.parametros()
                self.match('FECHA_PARENTESE')
            elif self.match('DOIS_PONTOS'):
                self.match('DOIS_PONTOS')
                self.tipo_retorno()
            else:
                self.atribuicao()
        else:
            print("Erro: Esperado ID apos o tipo de declaracao")

    def tipo_retorno(self):
        self.match('INTEIRO', 'BOOLEANO', 'VAZIO')

    def atribuicao(self):
        if self.match('ID'):
            if self.atual_token and self.atual_token[0] == 'ATRIBUICAO':
                self.match('ATRIBUICAO')
                self.token()
            elif self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
                self.lista_argumentos()
                if not self.match('FECHA_PARENTESE'):
                    raise Exception(f"Erro: Fecha parentese nao encontrado, mas encontrado {self.atual_token}.")
        else:
            raise Exception("Erro: Esperado 'ID' para atribuicao ou chamada de funcao")

    def if_condicional(self):
        if not self.match('SE'):
            raise Exception(f"Erro: 'SE' esperado, mas encontrado {self.atual_token}")

        self.parenteses_expressao()
        self.escopo()
        
        if self.atual_token is not None and self.atual_token[0] == 'SENAO':
            self.prox_token()
            self.escopo()   

    def break_condicional(self):
        self.match('INTERROMPER')

    def continue_condicional(self):
        self.match('CONTINUAR')

    def return_condicional(self):
        self.match('RETORNAR')
        if self.atual_token[0] == 'STRING':
            self.prox_token()
        while self.atual_token[0] == 'ID':
            self.prox_token()
            while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                self.prox_token()
                if self.atual_token[0] != 'ID':
                    raise ValueError("Erro: esperado 'ID' apos operador")
                self.prox_token()
        if self.atual_token[0] == 'NUMERO':
            self.prox_token()
        else:
            self.match("VIRGULA")

    def chamada_funcao(self):
        identifier = self.atual_token[1]
        self.match('ID')

        if self.atual_token != None and self.atual_token[0] == 'ABRE_PARENTESE':
            self.lista_argumentos()
            if self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                self.prox_token()
                if self.atual_token[0] == 'ATRIBUICAO':
                    self.prox_token()
                    if self.atual_token[0] == 'NUMERO' or self.atual_token[0] == 'ID':
                        self.prox_token()
                    elif self.atual_token[0] != ['ID', 'NUMERO']:
                        raise Exception("Erro: Atribuicao incorreta")
                if self.atual_token[0] == 'NUMERO' or self.atual_token[0] == 'ID':
                    self.prox_token()
                    if self.atual_token[0] != 'NUMERO' or self.atual_token[0] != 'ID':
                        while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                            self.prox_token()
                            if self.atual_token[0] != 'NUMERO' or self.atual_token[0] != "ID":
                                raise Exception("Erro: Expressao invalida apos a atribuicao de numero.")
                            else:
                                self.prox_token()
            
        elif self.atual_token != None and self.atual_token[0] == 'ATRIBUICAO':
            self.match('ATRIBUICAO')
            self.tratar_atribuicao()
            
        elif self.atual_token != None and self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
            self.prox_token()
            if self.atual_token[0] == 'ATRIBUICAO':
                self.prox_token()
                if self.atual_token[0] == 'NUMERO' or self.atual_token[0] == 'ID':
                    self.prox_token()
                elif self.atual_token[0] != ['ID', 'NUMERO']:
                    raise Exception("Erro: Atribuicao incorreta")
            if self.atual_token[0] == 'NUMERO' or self.atual_token[0] == 'ID':
                self.prox_token()
                if self.atual_token[0] != 'NUMERO' or self.atual_token[0] != 'ID':
                    while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                        self.prox_token()
                        if self.atual_token[0] != 'NUMERO' or self.atual_token[0] != "ID":
                            raise Exception("Erro: Expressao invalida apos a atribuicao de numero.")
                        else:
                            self.prox_token()
        else:
            raise Exception(f"Erro: Token inesperado {self.atual_token} apos a chamada da função {identifier}.")

    def tratar_atribuicao(self):
        if self.atual_token[0] == 'NUMERO':
            self.prox_token()
            while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                self.prox_token()
                if self.atual_token[0] != 'NUMERO' or self.atual_token[0] != 'ID':
                    raise Exception("Erro: Expressao invalida apos a atribuicao de numero.")
                else:
                    self.prox_token()
        elif self.atual_token[0] == 'ABRE_PARENTESE':
            self.prox_token()
            while self.atual_token[0] != 'FECHA_PARENTESE':
                self.prox_token()
                if self.atual_token[0] in ['NUMERO']:
                    self.prox_token()
                    if self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                        self.prox_token()
                        if self.atual_token[0] not in ['ID', 'NUMERO']:
                            raise Exception("Erro: Expressao invalida apos a atribuicao.")
                elif self.atual_token[0] == 'ID':
                    self.prox_token()
                    if self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                        self.prox_token()
                        if self.atual_token[0] not in ['ID', 'NUMERO']:
                            raise Exception("Erro: Expressao invalida apos a atribuicao.")
            self.prox_token()
            if self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                self.prox_token()
                if self.atual_token[0] == 'NUMERO' or self.atual_token[0] == 'ID':
                    self.prox_token()
                    if self.atual_token[0] != 'NUMERO' or self.atual_token[0] != 'ID':
                        while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                            self.prox_token()
                            if self.atual_token[0] != 'NUMERO' and self.atual_token[0] != "ID":
                                raise Exception("Erro: Expressao invalida apos a atribuicao de numero.")
                            else:
                                self.prox_token()

        elif self.atual_token[0] == 'BOOLEANO':
            self.prox_token()

        elif self.atual_token[0] == 'STRING':
            self.prox_token()
            while self.atual_token != None and self.atual_token[0] == 'MAIS':
                self.prox_token()
                if self.atual_token[0] != 'ID':
                    raise Exception("Erro: Impossivel concatenar, pois não existe variavel apos o +")
                self.prox_token()
            
        elif self.atual_token[0] == 'ID':
            self.prox_token()
            if self.atual_token[0] == 'ABRE_PARENTESE':
                self.prox_token()
                while self.atual_token != 'FECHA_PARENTESE':
                    if self.atual_token[0] == 'ID' or self.atual_token[0] == 'NUMERO':
                        self.prox_token()
                        if self.atual_token[0] == 'FECHA_PARENTESE':
                            break
                        if self.atual_token[0] == 'VIRGULA':
                            self.prox_token()
                        else:
                            raise Exception("Erro: Atribuicao errada")
            self.prox_token()
        else:
            raise Exception("Erro: Expressao inesperada apos a atribuicao.")

    def parametros(self):
        while self.match('ID'):
            if self.atual_token and self.atual_token[0] == 'VIRGULA':
                self.match('VIRGULA')
            else:
                break

    def lista_argumentos(self):
        if self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
            self.match('ABRE_PARENTESE')
            if self.atual_token and self.atual_token[0] in ['MAIOR', 'MENOR', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'IGUAL', 'DIFERENTE', 'NUMERO', 'ID', 'STRING', 'BOOLEANO', 'MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                self.expressao()
                while self.atual_token and self.atual_token[0] == 'VIRGULA':
                    self.match('VIRGULA')
                    self.expressao()
            if not self.match('FECHA_PARENTESE'):
                raise Exception("Erro: Esperado ')' para finalizar a lista de argumentos.")
        else:
            raise Exception("Erro: Esperado '(' para iniciar a lista de argumentos.")
        
    def abre_fecha_parenteses(self):
            if not self.match('ABRE_PARENTESE'):
                raise Exception(f"Erro: Abre parentese nao encontrado, mas encontrado {self.atual_token}.")
            self.parametros()
            if not self.match('FECHA_PARENTESE'):
                raise Exception(f"Erro: Fecha parentese nao encontrado, mas encontrado {self.atual_token}.")
            
    def escopo_funcao(self):
            if not self.match('ABRE_CHAVE'):
                raise Exception(f"Erro: Abre chaves nao encontrado, mas encontrado {self.atual_token}.")
            while self.atual_token[0] != 'FECHA_CHAVE':
                print(self.atual_token)
                if self.atual_token[0] == 'IMPRIMIR':
                    self.imprimir()
                elif self.atual_token[0] == 'SE':
                    self.if_condicional()
                elif self.atual_token[0] == 'ENQUANTO':
                    self.enquanto_condicional()
                elif self.atual_token[0] == 'ID':
                    self.chamada_funcao()
                if self.atual_token[0] == 'RETORNAR':
                    self.return_condicional()
                if self.atual_token[0] not in ['IMPRIMIR', 'SE', 'ENQUANTO', 'ID', 'RETORNAR', 'FECHA_CHAVE']:
                    raise Exception(f"Erro: Token inesperado {self.atual_token}")
            if not self.match('FECHA_CHAVE'):
                raise Exception(f"Erro: Fecha chaves nao encontrado, mas encontrado {self.atual_token}.")
            
    def declaracao_funcao(self):
        if not self.match('FUNCAO'):
            raise Exception(f"Erro: 'FUNCAO' esperado, mas encontrado {self.atual_token}")
        if not self.match('ID'):
            raise Exception(f"Erro: 'ID' esperado, mas encontrado {self.atual_token}")
        self.abre_fecha_parenteses()
        self.escopo_funcao()
        
        
        