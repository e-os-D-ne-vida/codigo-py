import random

N_Secreto = random.randint(1 , 50)
print(N_Secreto)
dica = input(" vc quer dica? (sim ou não): ")
if dica == "sim":
    if N_Secreto%2 == 0:
        print("O numero eh par")
    else:
        print("O numero é impar")
dica2 = input("vc quer outra dica (sim ou não): ")
if dica2 == "sim":
    if N_Secreto % 5 == 0 :
        print(" O número é multiplo de 5")
    else:
        print(" o número não é multiplo de 5")
# Lista de chutes
chutes = []

# Limite de tentativas
tentativas = 3

# Loop para controlar os chutes
for i in range(tentativas):
    # Pedindo o chute
    chute = int(input(f"Chute {i+1}: Digite seu chute de 1 a 50: "))
    chutes.append(chute)  # Adiciona o chute na lista

    # Verificando se o chute está correto
    if chute == N_Secreto:
        print("Parabéns, você acertou o número!")
        break  # Sai do loop se o chute for correto
    elif chute > N_Secreto:
        print("O número secreto é menor do que você pensa.")
    elif chute < N_Secreto:
        print("O número secreto é maior do que você pensa.")
    
    # Verificando se está "raspando" o número
    if abs(chute - N_Secreto) <= 5:
        print("Seu chute passou raspando!")

# Se o jogador não acertou o número, mostra a mensagem de derrota
if chutes[-1] != N_Secreto:
    print("Você perdeu!")

# Mostrando o número secreto no final
print(f"O número secreto era {N_Secreto}.")
