# Aula sobre operadores lógicos

# and: retorna True se ambas as condições forem verdadeiras;
# or: retorna True se pelo menos uma condição for verdadeira;
# not: inverte o valor lógico (True vira False e vice-versa).

# Se ele possui alta renda.
# Se ele possui bom crédito.

tem_alta_renda = True
tem_bom_credito = True

# Exemplo para and not
tem_historico_criminal = True

if tem_alta_renda and tem_historico_criminal:
    print("Elegível para empréstimo.")

