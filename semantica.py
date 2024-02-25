from tabelaSimbolos import TabelaDeSimbolos 
class Semantica:
    def __init__(self):
        self.tabela = {}

    def verificar_parametros(self, nome_variavel):
        pass 

    def verificar_retorno(self, nome_variavel):
        pass

    def verificar_atribuicao(self, nome_variavel, tipo_valor):
        print('nome_variavel', nome_variavel, 'tipo_valor', tipo_valor)
        tabelaSimbolos = TabelaDeSimbolos() 

        valor_variavel = nome_variavel[1]

        nome_variavel_tabela = tabelaSimbolos.obter_nome_por_valor(valor_variavel)
        
        lexema_variavel = tabelaSimbolos.obter_lexema(nome_variavel_tabela)

        if tipo_valor == 'VARIAVEL':
            # print('VARIAVEL + ',nome_variavel, '|', tipo_valor)
            return True
        
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
