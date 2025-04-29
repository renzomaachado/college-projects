ct=0
soma=0
media=0
for i in range (1,6,1):
    n=float(input('digite a nota do aluno:'))
    ct+=1
    soma+=n
media=soma/ct
print('a quantidade de notas dos alunos é:',ct)
print('a media das notas dos alunos é {:.1f}'.format(media))
print('o progama acabou.')
