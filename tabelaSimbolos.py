class TabelaDeSimbolos:
    def __init__(self):
        self.simbolos = {}

    def adicionar_simbolo(self, nome, tipo, linha):
        if nome not in self.simbolos:
            self.simbolos[nome] = {'tipo': tipo, 'linha': linha}

    def obter_tipo(self, nome):
        if nome in self.simbolos:
            return self.simbolos[nome]['tipo']

    def imprimir_tabela(self):
        print("Tabela de Simbolos:")
        print("------------------------------")
        print("| Nome\t| Tipo\t| Linha\t|")
        print("------------------------------")
        for nome, info in self.simbolos.items():
            print(f"| {nome}\t| {info['tipo']}\t| {info['linha']}\t|")
        print("------------------------------")