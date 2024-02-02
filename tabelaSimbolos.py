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

    def imprimir_tabela(self):
        print('\n')
        print("Tabela de Simbolos:" + '\n')
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                print(linha, end='')
        print()
