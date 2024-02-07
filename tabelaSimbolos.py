import re 
class TabelaDeSimbolos:

    def __init__(self):
        self.tabela = {}

    @staticmethod
    def tabelaSimbolos():
        tabelaSimbolos = {}
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                tabelaSimbolos[linha.split()[0]] = {'TIPO': linha.split()[1], 'VALOR': linha.split()[2], 'LEXEMA': linha.split()[3]}
        return tabelaSimbolos

    def adicionar_simbolo(self, nome, tipo, linha):
        if nome not in self.tabela:
            self.tabela[nome] = {'tipo': tipo, 'linha': linha}

    @staticmethod
    def obter_tipo(nome):
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                if re.search(f"^{nome}:", linha):
                    return linha.split(':')[2].strip()
        return None
        
    @staticmethod
    def obter_lexema(nome):
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                if re.search(f"^{nome}:", linha):
                    partes = linha.split(':')
                    if len(partes) >= 5:
                        return partes[4].strip().strip("{'").strip("'}")
        return None

    @staticmethod
    def obter_valor(nome):
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                if re.search(f"^{nome}:", linha):
                    return linha.split(':')[3].strip()
        return None

    def imprimir_tabela(self):
        print('\n')
        print("Tabela de Simbolos:" + '\n')
        tabelaSimbolos = TabelaDeSimbolos.tabelaSimbolos()
        for linha in tabelaSimbolos.values():
            print(linha)
        print()
