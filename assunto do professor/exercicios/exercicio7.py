# Solicite ao usuário o nome do aluno
# as 4 notas e mostre a média junto com o 
# nome do aluno usando o f-string

nome = str(input("Nome do Aluno :"))

nota1 = int (input("nota 1 :"))
nota2 = int (input("nota 2 :"))
nota3 = int (input("nota 3 :"))
nota4 = int (input("nota 4 :"))
soma = (nota1+nota2+nota3+nota4) /4
print
(f" Nome :{nome}\n Média do aluno é: {soma}")