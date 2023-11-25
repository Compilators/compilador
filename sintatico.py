import sys 
sys.path.append('../')
from lexico import analisador_lexico

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
            #print(f"Erro: Esperado {', '.join(tipo_token)}, mas encontrou {self.atual_token}")
            return False

    def programa(self):
        while self.atual_token:
            self.condicionais()

    def condicionais(self):
        if self.match('INTEIRO', 'BOOLEANO', 'VAZIO'):
            self.declaracao()
        elif self.match('SE'):
            self.if_condicional()
        elif self.match('SENAO'):
            self.else_condicional()
        elif self.match('ENQUANTO'):
            self.while_condicional()
        elif self.match('INTERROMPER'):
            self.break_condicional()
        elif self.match('CONTINUAR'):
            self.continue_condicional()
        elif self.match('IMPRIMIR'):
            self.echo_condicional()
        elif self.match('RETORNAR'):
            self.return_condicional()
        else:
            self.expressao_declaracao()

    def declaracao(self):
        if self.match('INTEIRO', 'BOOLEANO', 'VAZIO'):
            self.tipo_declaracao()
        else:
            self.match('ID')
            self.atribuicao()

    def tipo_declaracao(self):
        if self.match('ID'):
            if self.match('ABRE_PARENTESE'):
                self.lista_parametros()
                self.match('FECHA_PARENTESE')
            elif self.match('DOIS_PONTOS'):
                self.match('DOIS_PONTOS')
                self.tipo_especifico()
            else:
                self.atribuicao()
        else:
            print("Erro: Esperado ID após o tipo de declaração")

    def tipo_especifico(self):
        self.match('INTEIRO', 'BOOLEANO', 'VAZIO')

    def atribuicao(self):
        if self.match('ID'):
            if self.atual_token and self.atual_token[0] == 'ATRIBUICAO':
                self.match('ATRIBUICAO')
                self.expressao()
            elif self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
                self.lista_argumentos()
                self.match('FECHA_PARENTESE')
        else:
            print("Erro: Esperado 'ID' para atribuição ou chamada de função")

    def block(self):
        if not self.match('ABRE_CHAVE'):
            raise Exception(f"ABRE CHAVE não encontrado.")
        self.programa()
        if not self.match('FECHA_CHAVE'):
            raise Exception(f"FECHA CHAVE não encontrado.")

    def if_condicional(self):
        if not self.match('ABRE_PARENTESE'):
            raise Exception(f"Abre parêntese não encontrado.")
        self.expressao()
        if not self.match('FECHA_PARENTESE'):
            raise Exception(f"Fecha parêntese não encontrado.")
        self.condicionais()
        if self.match('SENAO'):
            self.condicionais()


    def else_condicional(self):
        self.condicionais()

    def while_condicional(self):
        if not self.match('ABRE_PARENTESE'):
            raise Exception(f"Abre parêntese não encontrado.")
        self.expressao()
        if not self.match('FECHA_PARENTESE'):
            raise Exception(f"Fecha parêntese não encontrado.")

    def break_condicional(self):
        self.match('INTERROMPER')

    def continue_condicional(self):
        self.match('CONTINUAR')

    def echo_condicional(self):
        self.match('STRING')

    def return_condicional(self):
        self.match('RETORNAR')
        self.expressao()

    def expressao_declaracao(self):
        self.expressao()

    def expressao(self):
        if self.atual_token and self.atual_token[0] == 'NUMERO':
            self.prox_token()
        elif self.atual_token and self.atual_token[0] == 'ID':
            self.atribuicao_or_function_call()
        elif self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
            self.match('ABRE_PARENTESE')
            self.expressao()
            self.match('FECHA_PARENTESE')
        elif self.atual_token and self.atual_token[0] == 'FUNCAO':
            self.funcao_declaracao()
        elif self.atual_token and self.atual_token[0] == 'STRING':
            self.match('STRING')
        elif self.atual_token and self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
            self.prox_token()
            self.expressao()
        elif self.atual_token and self.atual_token[0] == 'ATRIBUICAO':
            self.prox_token()
            self.expressao()
        else:
            print(f"Erro: Expressao invalida. Encontrou {self.atual_token}")

        while self.atual_token and self.atual_token[0] in ['MAIOR', 'MENOR', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'IGUAL', 'DIFERENTE']:
            self.prox_token()
            self.expressao()


    def atribuicao_or_function_call(self):
        identifier = self.atual_token[1]
        self.match('ID')
        if self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
            self.match('ABRE_PARENTESE')
            self.lista_argumentos()
            self.match('FECHA_PARENTESE')
        elif self.atual_token and self.atual_token[0] == 'ATRIBUICAO':
            self.match('ATRIBUICAO')
            self.expressao()

    def lista_parametros(self):
        while self.match('ID'):
            if self.atual_token and self.atual_token[0] == 'VIRGULA':
                self.match('VIRGULA')
            else:
                break


    def lista_argumentos(self):
        while self.atual_token and self.atual_token[0] != 'FECHA_PARENTESE':
            self.expressao()
            if self.atual_token and self.atual_token[0] == 'VIRGULA':
                self.match('VIRGULA')
            else:
                break

    def funcao_declaracao(self):
        if not self.match('FUNCAO'):
            raise Exception(f"Erro: 'FUNCAO' esperado, mas encontrado {self.atual_token}")
        if not self.match('ID'):
            raise Exception(f"Erro: 'ID' esperado, mas encontrado {self.atual_token}")
        if not self.match('ABRE_PARENTESE'):
            raise Exception(f"Erro: Abre parêntese não encontrado, mas encontrado {self.atual_token}.")
        self.lista_parametros()
        if not self.match('FECHA_PARENTESE'):
            raise Exception(f"Erro: Fecha parêntese não encontrado, mas encontrado {self.atual_token}.")

# Codigo fonte 
codigo_fonte = """
variavel_inteira = 5
variavel_booleana = verdadeiro

funcao imprimir_ola():
    imprimir("Ola, Mundo!")

funcao somar(a, b):
    retornar a + b

resultado = 0

imprimir_ola()

resultado = somar(3, 4)

se (resultado > 10):
    imprimir("Resultado e maior que 10.")
senao:
    imprimir("Resultado e 10 ou menor.")

contador = 0
enquanto (contador < resultado):
    imprimir(f"Contando: {contador}")
    contador += 1

    se (contador == 5):
        imprimir("Pulando 5")
        continuar
    
    se (contador == 7):
        imprimir("Parando no 7")
        interromper

MINHA_CONSTANTE = "Esta e uma constante"
imprimir(MINHA_CONSTANTE)

imprimir(f"Variável booleana: {variavel_booleana}")

resultado_aritmetico = (variavel_inteira + resultado) - 5 * 2 / 2

se (resultado_aritmetico == 10):
    imprimir("Alguma condicao booleana foi atendida.")
"""

tokens = analisador_lexico(codigo_fonte)
Sintatico = Sintatico(iter(tokens))
Sintatico.programa()
