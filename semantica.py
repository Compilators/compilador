from tabelaSimbolos import TabelaDeSimbolos 
class Semantica:
    def __init__(self):
        self.tabela = {}

    def verificar_parametros(self, nome_funcao, linha):
        pass 

    def verificar_retorno(self, nome_funcao, linha):
        pass

    def verificar_atribuicao(self, nome_variavel):
        tabelaSimbolos = TabelaDeSimbolos()
        print('entrou')
        if tabelaSimbolos.obter_lexema(nome_variavel) == None:
            return True
        else:
                if nome_variavel.isdigit():
                    if tabelaSimbolos.obter_lexema(nome_variavel) == 'NUMERO':
                        return True
                    else:
                        return False
                elif nome_variavel.isalpha():
                    if tabelaSimbolos.obter_lexema(nome_variavel) == 'STRING':
                        return True
                    else:
                        return False
                elif nome_variavel == 'verdadeiro' or nome_variavel == 'falso':
                    if tabelaSimbolos.obter_lexema(nome_variavel) == 'BOOLEANO':
                        return True
                    else:
                        return False
        pass 

    def verificar_condicional(self, condicao, linha):
        pass

    def verificar_interromper(self, linha):
        pass

    def verificar_continuar(self, linha):
        pass

    def verificar_imprimir(self, valor, linha):
        pass 

    def verificar_booleano(self, nome_variavel, linha):
        pass 

    def verificar_inteiro(self, nome_variavel, linha):
        pass