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

    def match(self, *tipos_token):
        if self.atual_token and self.atual_token[0] in tipos_token:
            self.prox_token()
            return True
        else:
            print(f"Erro: Esperado {', '.join(tipos_token)}, mas encontrou {self.atual_token}")
            return False

    def programa(self):
        while self.atual_token:
            self.statement()

    def declaracao_global(self):
        if self.match('INTEIRO', 'BOOLEANO', 'VAZIO'):
            self.declaracao()
        elif self.match('SE'):
            self.if_declaracao()
        elif self.match('ENQUANTO'):
            self.while_declaracao()
        elif self.match('INTERROMPER'):
            self.break_declaracao()
        elif self.match('CONTINUAR'):
            self.continue_declaracao()
        elif self.match('IMPRIMIR'):
            self.echo_declaracao()
        elif self.match('RETORNAR'):
            self.return_declaracao()
        else:
            self.expression_declaracao()
            

    def declaracao(self):
        if self.match('INTEIRO', 'BOOLEANO', 'VAZIO'):
            self.declaracao_tipo()
        else:
            self.match('ID')
            self.assignment()
            self.match('PONTO_E_VIRGULA')

    def declaracao_tipo(self):
        if self.match('ID'):
            if self.match('ABRE_PARENTESE'):
                self.parameter_list()
                self.match('FECHA_PARENTESE')
                self.block()
            elif self.match('DOIS_PONTOS'):
                self.match('DOIS_PONTOS')
                self.tipo_especifico()
                self.match('PONTO_E_VIRGULA')
            elif self.match('PONTO_E_VIRGULA'):
                pass
            else:
                self.assignment()
                self.match('PONTO_E_VIRGULA')
        else:
            print("Erro: Esperado ID após o tipo de declaração")

    def tipo_especifico(self):
            self.match('INTEIRO', 'BOOLEANO', 'VAZIO')


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

se resultado > 10:
    imprimir("Resultado e maior que 10.")
senao:
    imprimir("Resultado e 10 ou menor.")

contador = 0
enquanto contador < resultado:
    imprimir(f"Contando: {contador}")
    contador += 1

    se contador == 5:
        imprimir("Pulando 5")
        continuar
    
    se contador == 7:
        imprimir("Parando no 7")
        interromper

MINHA_CONSTANTE = "Esta e uma constante"
imprimir(MINHA_CONSTANTE)

imprimir(f"Variável booleana: {variavel_booleana}")

resultado_aritmetico = (variavel_inteira + resultado) - 5 * 2 / 2

se resultado_aritmetico == 10 ou (variavel_inteira != 5 e variavel_booleana e resultado <= 10):
    imprimir("Alguma condicao booleana foi atendida.")
"""