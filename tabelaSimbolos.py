class TabelaDeSimbolos:
    def __init__(self):
        self.tabela = {}

    def adicionar_simbolo(self, nome, tipo, linha):
        if nome not in self.tabela:
            self.tabela[nome] = {'tipo': tipo, 'linha': linha}

    def obter_tipo(self, nome):
        if nome in self.tabela:
            return self.tabela[nome]['tipo']
        else:
            return None

    def verificar_parametros(self, nome_funcao, linha):
        pass 

    def verificar_retorno(self, nome_funcao, linha):
        pass

    def verificar_atribuicao(self, nome_variavel, linha):
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

    def imprimir_tabela(self):
        print('\n')
        print("Tabela de Simbolos:" + '\n')
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                print(linha, end='')
        print()