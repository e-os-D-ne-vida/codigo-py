# #printa numeros pares pela caixaP e numeros impares pela caixaI
# caixaP = [ ]
# caixaI = [ ]
# for i in range(101):
#     if i%2 == 0:
#         caixaP.append(i)
#     else:
#         caixaI.append(i)

# print(caixaP)
# print(caixaI)
# #printa uma lista ao contrario
# for numero in range( 10 , 0 , -1):
#    print(numero)

# #soma os numeros de uma lista
# lista = [10 , 20 , 30 , 40 , 50]
# Soma = 0
# for i in lista:
#     Soma += i
# print (Soma)

# #printa os caracteres de uma variavel
# texto = "python"
# for palavra in texto:
#    print( palavra )

# #inverte os caracteres de uma string e depois printa
# texto2  = "Saudade da minha mulher"
# texto_I = texto2 [:: -1]
# for palavra_I in texto_I:
#     print(palavra_I)

# #multiplicar os numeros de uma lista
# numeros = [2, 4, 6, 8]
# produto = 1
# for P in numeros:
#     produto *= P
# print (produto)

# #serve pra printar uma lista e dizer seu indice
# recado = ["eu" , "amo" , "o" , "amor" , "da" , "minha" , "vida" , 2 , 3,4,4 , "a"]
# for N , T in enumerate(recado):
#     print(f"A posição eh {N} e o texto eh {T}")
# #serve pra separar uma variavel e dizer seu indice
# # o I sozinho é o indice e quando vem junto com a variavel {recado2[I] , eh o texto}
recado2 = "eu amo minha namorada"
for I  in range(len(recado2)):
    print(f"indice: {I}, caraceter: {recado2[I]}")

# #serve para dizer o numero de espaços
# N_Espaços = 0
# for i in range(len(recado2)):
#     if recado2[i] == ' ' :
#         N_Espaços += 1

# print (N_Espaços)
S_Espaço = " "

#serve pra tirar o espaço
for T_Espaço in range(len(recado2)):
    if recado2[T_Espaço] != ' ':
        S_Espaço += recado2[T_Espaço]
print(S_Espaço)
# serve para imprimir N numeros N vezes 
#for i in range(1, 100):
   # print(str(i) * i)