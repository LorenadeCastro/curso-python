nome = 'Ana'
sobrenome = 'Silva'
# essa forma deixa o código "feio" mensagem = nome + ' [' + sobrenome +'] é aluna nova.'#

# forma mais limpa
mensagem = f'{nome} {sobrenome} é aluna nova.'
print(mensagem)