import os
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
            # print(f"Erro: Esperado {', '.join(tipo_token)}, mas encontrou {self.atual_token}")
            return False

    def programa(self):
        while self.atual_token:
            self.token()
            if self.atual_token is None:
                print("Compilacao finalizada com sucesso.")
                break

    def token(self):
        print(self.atual_token)
        match self.atual_token[0]:
            case 'ID':
                self.atribuicao_ou_chamada_funcao()
            case 'FUNCAO':
                self.funcao_declaracao()
            case 'SE':
                self.if_condicional()
            case 'ENQUANTO':
                self.enquanto_condicional()
            case 'IMPRIMIR':
                self.imprimir()
            case _:
                print(f"Erro: Expressao invalida. Encontrou {self.atual_token}")
                sys.exit(1)

    def enquanto_condicional(self):
        if not self.match('ENQUANTO'):
            raise Exception(f"Erro: 'ENQUANTO' esperado, mas encontrado {self.atual_token}")

        if not self.match('ABRE_PARENTESE'):
            raise Exception(f"Abre parentese nao encontrado.")

        self.lista_argumentos()

        if not self.match('FECHA_PARENTESE'):
            raise Exception(f"Fecha parentese nao encontrado.")

        if not self.match('ABRE_CHAVE'):
            raise Exception(f"Erro: Abre chaves nao encontrado, mas encontrado {self.atual_token}.")

        while self.atual_token[0] == 'IMPRIMIR':
            self.imprimir()

        while self.atual_token[0] == 'SE':
            self.if_condicional()

        while self.atual_token[0] == 'ENQUANTO':
            self.enquanto_condicional()

        while self.atual_token[0] == 'ID':
            self.atribuicao_ou_chamada_funcao()

        if self.atual_token[0] == 'CONTINUAR':
            self.continue_condicional()
        elif self.atual_token[0] == 'INTERROMPER':
            self.break_condicional()

        if not self.match('FECHA_CHAVE'):
            raise Exception(f"Erro: Fecha chaves nao encontrado, mas encontrado {self.atual_token}.")
        self.token()

    def imprimir(self):
        if self.match('IMPRIMIR'):
            self.match('ABRE_PARENTESE')
            while self.atual_token[0] in ['MAIOR', 'MENOR', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'IGUAL', 'DIFERENTE', 'NUMERO', 'ID', 'STRING', 'BOOLEANO', 'MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                self.prox_token()
            self.match('FECHA_PARENTESE')
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
                self.lista_parametros()
                self.match('FECHA_PARENTESE')
            elif self.match('DOIS_PONTOS'):
                self.match('DOIS_PONTOS')
                self.tipo_especifico()
            else:
                self.atribuicao()
        else:
            print("Erro: Esperado ID apos o tipo de declaracao")

    def tipo_especifico(self):
        self.match('INTEIRO', 'BOOLEANO', 'VAZIO')

    def atribuicao(self):
        if self.match('ID'):
            if self.atual_token and self.atual_token[0] == 'ATRIBUICAO':
                self.match('ATRIBUICAO')
                self.token()
            elif self.atual_token and self.atual_token[0] == 'ABRE_PARENTESE':
                self.lista_argumentos()
                self.match('FECHA_PARENTESE')
        else:
            print("Erro: Esperado 'ID' para atribuicao ou chamada de funcao")

    def if_condicional(self):
        if not self.match('SE'):
            raise Exception(f"Erro: 'SE' esperado, mas encontrado {self.atual_token}")

        if not self.match('ABRE_PARENTESE'):
            raise Exception(f"Abre parentese nao encontrado.")

        self.lista_argumentos()

        if not self.match('FECHA_PARENTESE'):
            raise Exception(f"Fecha parentese nao encontrado.")

        if not self.match('ABRE_CHAVE'):
            raise Exception(f"Erro: Abre chaves nao encontrado, mas encontrado {self.atual_token}.")

        while self.atual_token[0] == 'IMPRIMIR':
            self.imprimir()

        while self.atual_token[0] == 'SE':
            self.if_condicional()

        while self.atual_token[0] == 'ENQUANTO':
            self.enquanto_condicional()

        while self.atual_token[0] == 'ID':
            self.atribuicao_ou_chamada_funcao()

        if self.atual_token[0] == 'CONTINUAR':
            self.continue_condicional()
        elif self.atual_token[0] == 'INTERROMPER':
            self.break_condicional()

        if not self.match('FECHA_CHAVE'):
            raise Exception(f"Erro: Fecha chaves nao encontrado, mas encontrado {self.atual_token}.")

        elif self.atual_token is not None and self.atual_token[0] == 'SENAO':
            self.prox_token()
            if not self.match('ABRE_CHAVE'):
                raise Exception(f"Erro: Abre chaves nao encontrado, mas encontrado {self.atual_token}.")

            while self.atual_token[0] == 'IMPRIMIR':
                self.imprimir()

            while self.atual_token[0] == 'SE':
                self.if_condicional()

            while self.atual_token[0] == 'ENQUANTO':
                self.enquanto_condicional()

            while self.atual_token[0] == 'ID':
                self.atribuicao_ou_chamada_funcao()
            if not self.match('FECHA_CHAVE'):
                raise Exception(f"Erro: Fecha chaves nao encontrado, mas encontrado {self.atual_token}.")

    def break_condicional(self):
        self.match('INTERROMPER')

    def continue_condicional(self):
        self.match('CONTINUAR')

    def echo_condicional(self):
        self.match('STRING')

    def return_condicional(self):
        self.match('RETORNAR')
        if self.atual_token[0] == 'STRING':
            self.prox_token()
        while self.atual_token[0] == 'ID':
            self.prox_token()
            if self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
                self.prox_token()
        if self.atual_token[0] == 'NUMERO':
            self.prox_token()
        else:
            self.match("VIRGULA")

    def atribuicao_ou_chamada_funcao(self):
        identifier = self.atual_token[1]
        self.match('ID')
        if self.atual_token[0] == 'ABRE_PARENTESE':
            self.match('ABRE_PARENTESE')
            self.lista_argumentos()
            self.match('FECHA_PARENTESE')
        elif self.atual_token[0] == 'ATRIBUICAO':
            self.match('ATRIBUICAO')
            if self.atual_token[0] == 'NUMERO':
                self.prox_token()
                while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE', 'NUMERO']:
                    self.prox_token()
            elif self.atual_token[0] == 'ABRE_PARENTESE':
                self.prox_token()
                while self.atual_token[0] != 'FECHA_PARENTESE':
                    self.token()
                self.prox_token()
                while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE', 'NUMERO']:
                    self.prox_token()
            elif self.atual_token[0] == 'BOOLEANO':
                self.prox_token()
            elif self.atual_token[0] == 'STRING':
                self.prox_token()
        elif self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
            self.prox_token()
            if self.atual_token[0] == 'ATRIBUICAO':
                self.prox_token()
                while self.atual_token[0] in ['MAIS', 'MENOS', 'VEZES', 'DIVIDE', 'NUMERO']:
                    self.prox_token()

    def lista_parametros(self):
        while self.match('ID'):
            if self.atual_token and self.atual_token[0] == 'VIRGULA':
                self.match('VIRGULA')
            else:
                break

    def lista_argumentos(self):
        while self.atual_token[0] in ['MAIOR', 'MENOR', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'IGUAL', 'DIFERENTE', 'NUMERO', 'ID', 'STRING', 'BOOLEANO', 'MAIS', 'MENOS', 'VEZES', 'DIVIDE']:
            self.prox_token()
            if self.atual_token and self.atual_token[0] == 'VIRGULA':
                self.match('VIRGULA')

    def funcao_declaracao(self):
        if not self.match('FUNCAO'):
            raise Exception(f"Erro: 'FUNCAO' esperado, mas encontrado {self.atual_token}")
        if not self.match('ID'):
            raise Exception(f"Erro: 'ID' esperado, mas encontrado {self.atual_token}")
        if not self.match('ABRE_PARENTESE'):
            raise Exception(f"Erro: Abre parentese nao encontrado, mas encontrado {self.atual_token}.")
        self.lista_parametros()
        if not self.match('FECHA_PARENTESE'):
            raise Exception(f"Erro: Fecha parentese nao encontrado, mas encontrado {self.atual_token}.")
        if not self.match('ABRE_CHAVE'):
            raise Exception(f"Erro: Abre chaves nao encontrado, mas encontrado {self.atual_token}.")
        while self.atual_token[0] == 'IMPRIMIR':
            self.imprimir()
        while self.atual_token[0] == 'SE':
            self.if_condicional()
        while self.atual_token[0] == 'ENQUANTO':
            self.enquanto_condicional()
        while self.atual_token[0] == 'ID':
            self.atribuicao_ou_chamada_funcao()
        if self.atual_token[0] == 'RETORNAR':
            self.return_condicional()
        if not self.match('FECHA_CHAVE'):
            raise Exception(f"Erro: Fecha chaves nao encontrado, mas encontrado {self.atual_token}.")

# Codigo fonte
codigo_fonte = """
variavel_inteira = 5
variavel_booleana = verdadeiro

funcao imprimir_ola(){
    imprimir("Ola, Mundo!")
}

funcao somar(a, b){
    retornar a + b
}
resultado = 0

imprimir_ola()

resultado = somar(3, 4)

se (resultado > 10){
    imprimir("Resultado e maior que 10.")
}
senao{
    imprimir("Resultado e 10 ou menor.")
}
contador = 0
enquanto (contador < resultado){
    imprimir("Contando: {contador}")
    contador += 1
    }
    se (contador == 5){
        imprimir("Pulando 5")
        continuar
    }
    se (contador == 7){
        imprimir("Parando no 7")
        interromper
    }

MINHA_CONSTANTE = "Esta e uma constante"
imprimir(MINHA_CONSTANTE)

imprimir("Variavel booleana: {variavel_booleana}")

resultado_aritmetico = (variavel_inteira + resultado) - 5 * 2 / 2

se (resultado_aritmetico == 10){
    imprimir("Alguma condicao booleana foi atendida.")
}
"""

# Cria um arquivo com o codigo fonte e outro com os tokens
diretorio_arquivo = os.path.dirname(os.path.realpath(__file__))
os.chdir(diretorio_arquivo)

arquivo_tokens = "tokens.txt"
tokens = analisador_lexico(codigo_fonte)

with open(arquivo_tokens, 'w') as arquivo:
    for token in tokens:
        arquivo.write(f"{token[0]}: {token[1]}\n")

with open("codigo_fonte.txt", 'w') as arquivo_saida:
    arquivo_saida.write(codigo_fonte)

Sintatico = Sintatico(iter(tokens))
Sintatico.programa()