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
    def contaOcorrencias(self, nome):
        contador = 0
        if nome in self.tabela:
            contador += 1
        if nome + '_nova' in self.tabelaSimbolos():
            contador += 1
        return contador
        
    
    @staticmethod
    def obter_nome_por_valor(valor):
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                if re.search(f"{valor}", linha):
                    return linha.split(':')[0]
        return None


    @staticmethod
    def obter_tipo(nome):
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                if re.search(f"^{nome}:", linha):
                    return linha.split 
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
        with open("tabela_simbolos.txt", 'r') as arquivo:
            for linha in arquivo:
                print(linha.strip())
