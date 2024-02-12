from tabelaSimbolos import TabelaDeSimbolos 
class Semantica:
    def __init__(self):
        self.tabela = {}

    def verificar_parametros(self, nome_funcao, linha):
        pass 

    def verificar_retorno(self, nome_funcao, linha):
        pass

    def verificar_atribuicao(self, nome_variavel, tipo_valor):
        tabelaSimbolos = TabelaDeSimbolos() 

        valor_variavel = nome_variavel[1]

        lexema_variavel = tabelaSimbolos.obter_nome_por_valor(valor_variavel)

        print(f'Nome da variavel: {lexema_variavel}')

        if lexema_variavel is None:
            return True 
        else:
            if tipo_valor == 'NUMERO' and lexema_variavel == 'NUMERO':
                return True
            elif tipo_valor == 'STRING' and lexema_variavel == 'STRING':
                return True
            elif tipo_valor == 'BOOLEANO' and lexema_variavel == 'BOOLEANO':
                return True
            else:
                return False

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