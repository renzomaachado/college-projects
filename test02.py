ct=0
soma=0
n1=int(input('digite o valor inicial da sequência:'))
n2=int(input('digite o valor final da sequencia:'))
if n1<n2:
    print('\nvalores na ordem crescente:\n')
    for i in range (n1 , n2+1 , 1):
        print(i, end=" \n")
        ct+=1
        soma+=i
elif n1>n2:
    print('\nvalores na ordem decrescente:\n')
    for i in range (n1 , n2-1, -1):
        print(i, end=" \n")
        ct+=1
        soma+=i
else:
    print('os valores que você digitou são iguais!')
print('\na quantiadede dos valores é:',ct)
print('a soma dos valores é:',soma)
print('o progama encerrou.')