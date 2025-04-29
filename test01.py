ct=0
soma=0
n1=int(input('digite o valor inicial da sequência:'))
n2=int(input('digite o valor final da sequencia:'))
print('sequencia dos numeros dados pelo cliente:' )
for i in range (n1,n2+1,1):
    print(i, end=" ")
    ct+=1
    soma+=i
print('\n a quantiadede dos valores é:',ct)
print('a soma dos valores é:',soma)
print('o progama encerrou.')
