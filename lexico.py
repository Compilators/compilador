# CÓDIGO FONTE 
codigo_fonte = """
variavel_inteira = 5
variavel_booleana = verdadeiro

funcao imprimir_ola():
    imprimir("Ola, Mundo!")

funcao somar(a, b):
    retornar a + b

resultado = 0

imprimir_ola()

resultado = somar(3, 4)

se resultado > 10:
    imprimir("Resultado e maior que 10.")
senao:
    imprimir("Resultado e 10 ou menor.")

contador = 0
enquanto contador < resultado:
    imprimir(f"Contando: {contador}")
    contador += 1

    se contador == 5:
        imprimir("Pulando 5")
        continuar
    
    se contador == 7:
        imprimir("Parando no 7")
        interromper

MINHA_CONSTANTE = "Esta e uma constante"
imprimir(MINHA_CONSTANTE)

imprimir(f"Variável booleana: {variavel_booleana}")

resultado_aritmetico = (variavel_inteira + resultado) - 5 * 2 / 2

se resultado_aritmetico == 10 ou (variavel_inteira != 5 e variavel_booleana e resultado <= 10):
    imprimir("Alguma condicao booleana foi atendida.")
"""