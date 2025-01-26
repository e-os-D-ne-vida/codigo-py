import random
import os

def Pega_input():
    print("Vamos criar um nome de super-herói pra você, aproveite!")
    M_G = input("Qual é o seu pronome (O ou A)?: ").strip().upper()  # Garantir que seja O ou A
    poder = input("Escreva o poder de seu super-herói: ").capitalize()
    adjetivo = input("Escreva um adjetivo: ").capitalize()
    tema = input("Escreva o tema: ").capitalize()
    return poder, adjetivo, tema, M_G

def faz_Nome(poder, adjetivo, tema, M_G):
    if M_G == "O":
        print("Entrando no bloco do pronome masculino")
        poder_L = ["invisibilidade", "teletransportador", "super honestidade", poder]
        adjetivo_L = ["O heroico" ,"O alto", "O burro", "O genioso","O" + adjetivo]
        tema_L = ["espacial", "viajante", "apocalíptico",tema]
    else:
        print("Entrando no bloco do pronome feminino")
        poder_L = ["invisibilidade", "teletransportadora", "super honestidade", poder]
        adjetivo_L = ["A heroica","A alta", "A burra", "A geniosa", adjetivo]
        tema_L = ["viajante", "apocalíptica", tema]

    palavra1 = random.choice(poder_L)
    palavra2 = random.choice(adjetivo_L)
    palavra3 = random.choice(tema_L)
    return palavra2.capitalize() + " " + palavra1 + " " + palavra3

# Obter os dados do usuário
poder, adjetivo, tema , M_G = Pega_input()

# Gerar o nome do herói
nome_gerado = faz_Nome(poder, adjetivo, tema, M_G)

# Imprimir o nome gerado
print(nome_gerado)

# Salvar o nome gerado em um arquivo
with open("Nome_Herois.txt", "a") as arquivo:
    arquivo.write("O nome é:\n")
    arquivo.write(f"{nome_gerado}\n")

print("Nome salvo em Nome_Herois.txt")

# Imprimir o diretório atual onde o arquivo está sendo salvo
print("O arquivo será salvo no diretório:", os.getcwd())
