ct=0
soma=0
maior_nota=-999999
menor_nota=999999
aprovado=0
n2=int(input('digite a quantidade de alunos:'))
for i in range (1,n2+1,1):
    n=float(input(f'digite a nota do aluno {i} :'))
    if n<menor_nota:
        menor_nota=n
    if n>maior_nota:
        maior_nota=n
    if n>= 5:
        aprovado+=1
    ct+=1
    soma+=n
print('a quantidade de notas dos alunos é:',ct)
print('a media das notas dos alunos é {:.2f}'.format(soma/ct))
print('a maior nota da turma é:',maior_nota)
print('a menor nota da turma é:',menor_nota)
print('a quantidade de alunos aprovados é:',aprovado)
print('o progama acabou.')
