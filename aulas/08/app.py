# Aula sobre funções

# len: quantidade de caracteres (também considera os espaços entre as palavras)
# upper: para deixar as letras maiúsculas
# lower: para deixar as letras minúsculas
# find : mostra em qual posição está a letra escolhi - lembrando que se inicia com zero, então a primeira letra (P) vai aparecer na posição zero. Ele diferencia letras minúsculas e maiúsculas, então, se eu colocar a letra p, como não tem p minúscula na minha frase, ele vai me retornar número negativo.
# find: também serve para mostrar a posição que se inicia determinada palavra
# replace: serve para substituir expressões
# in: serve para pesquisar um valor dentro do texto, afirmação boleana (verdadeiro ou falso - true ou false). Ficar atento quanto a forma escrita da palavra. Por exemplo: se eu escrever "python" com letra minúscula, ele vai me retornar "False", porque na minha frase não tem "Python" escrito com p minúsculo

curso = 'Python é legal.'
print(len(curso))
print(curso.upper())
print(curso.lower())
print(curso)
print(curso.find('P'))
print(curso.find('legal'))
print(curso.find('p'))
print(curso.replace('legal' , 'muito legal'))
print('Python' in curso)
print('python' in curso)