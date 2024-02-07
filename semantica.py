class Semantica:
    def __init__(self, tabela_simbolos):
        self.tabela = {}
        self.tabela_simbolos = tabela_simbolos

    def verificar_parametros(self, nome_funcao, linha):
        pass 

    def verificar_retorno(self, nome_funcao, linha):
        pass

    def verificar_atribuicao(self, nome_variavel, linha):
        posicao = linha
        while(self.tabela_simbolos[posicao] != '\n'):
            posicao = posicao + 1
            if(self.tabela_simbolos[posicao] == nome_variavel):
                while(self.tabela_simbolos[posicao] != '\n'):
                    posicao = posicao + 1
                    if(self.tabela_simbolos[posicao] == '='):
                        posicao = posicao + 1
                        if(self.tabela_simbolos[posicao].isdigit()):
                            if self.tabela_simbolos[posicao] in self.tabela_simbolos:
                                if self.tabela_simbolos[posicao]['LEXEMA'] == 'NUMERO':
                                    return True
                                else:
                                    return False
                            else :
                                return True
                        elif (self.tabela_simbolos[posicao].isalpha()):
                            if self.tabela_simbolos[posicao] in self.tabela_simbolos:
                                if self.tabela_simbolos[posicao]['LEXEMA'] == 'STRING':
                                    return True
                                else:
                                    return False
                            else :
                                return True
                        elif (self.tabela_simbolos[posicao] == 'verdadeiro' or self.tabela_simbolos[posicao] == 'falso'):
                            if self.tabela_simbolos[posicao] in self.tabela_simbolos:
                                if self.tabela_simbolos[posicao]['LEXEMA'] == 'BOOLEANO':
                                    return True
                                else:
                                    return False
                            else :
                                return True
                        else:
                            return False
                    else:
                        return False
            posicao = posicao + 1
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