# Aula sobre estruturas condicionais

# Nas condicionais utilizamos o True ou false (Verdadeiro ou Falso):
# if: executa um bloco de código se a condição for verdadeira;
# elif (abreviação de 'else if'): Permite verificar múltiplas condições em sequência. Pode haver vários elif;
# else: Captura todos os casos que não satisfizeram as condições if ou elif.
# Estrutura: Usa dois pontos (:) e indentação obrigatória para definir os blocos de código.


# Se o dia está quente
# O dia está quente.
# Beba água.

# Se o dia está frio.
# O dia está frio.
# Use agasalho.

# Se o dia não está quente, nem frio.
# É um belo dia!

esta_quente = False
esta_frio = True

if esta_quente:
    print("O dia está quente.")
    print("Beba água.")
elif esta_frio:
    print("O dia está frio.")
    print("Use agasalho.")
else:
    print("É um lindo dia!")
    
print("Tenha um bom dia!")