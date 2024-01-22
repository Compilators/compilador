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
        print("Tabela de Simbolos:")
        for nome, info in self.tabela.items():
            print(f"Nome: {nome}, Tipo: {info['tipo']}, Linha: {info['linha']}")