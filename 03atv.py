print('sequencia do dobro dos numeros naturais ate 10')
ct=0
soma=0
media=0
for i in range (1,11,):
    print(i,end=' --> ' )
    print(i*2)

    ct+=1
    soma+= i*2
media= soma /ct
print('a media dos valores é:',media)
print('a soma dos valores é:',soma)
print('o progama encerrou.')

