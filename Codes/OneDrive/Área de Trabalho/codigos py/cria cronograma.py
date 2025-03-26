from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

def obter_entrada_hora(prompt):
    while True:
        hora = input(prompt)
        if hora == "24:00":
            return datetime.strptime("00:00", "%H:%M")  # Trata "24:00" como "00:00"
        try:
            return datetime.strptime(hora, "%H:%M")
        except ValueError:
            print("Formato inválido! Por favor, insira no formato H:M.")

def Pega_Tarefa():
    tarefa = input("Digite sua tarefa: ")
    importancia = input("Digite qual é o grau de importância da tarefa (1 a 5): ")
    horas = obter_entrada_hora("Digite quanto tempo você usará nessa tarefa (H:M): ")

    return tarefa, horas.strftime("%H:%M"), importancia

def Converte_Hora(horas_str): #transforma string H:M em float
    try:
        horas, minutos = map(int, horas_str.split(":"))
        return horas + minutos / 60
    except ValueError:
        print("Valor de horas inválido, digite como H:M")
        return 0  # Retorna 0 caso a conversão falhe

def Calcula_duracao(horario_começo, horario_fim):
    # Garantir que os horários sejam válidos
    if horario_começo == "24:00":
        horario_começo = "00:00"
    if horario_fim == "24:00":
        horario_fim = "00:00"

    Começo = datetime.strptime(horario_começo, "%H:%M")
    Fim = datetime.strptime(horario_fim, "%H:%M")

    if Fim < Começo:  # Se o horário de fim for antes, considera-se o dia seguinte
        duração = (Fim - Começo + timedelta(days=1)).total_seconds() / 3600
    else:
        duração = (Fim - Começo).total_seconds() / 3600

    # Se os horários de início e fim forem iguais, retorna 24 horas
    if Começo == Fim:
        return 24.0  # Retorna como número flutuante para compatibilidade

    return duração

def Calcula_intervalo(horario_total_A, duração , Pausa):
    if horario_total_A > duração:
        print("Você não tem tempo suficiente para realizar todas as tarefas.")
        exit()
    return duração - (horario_total_A + Pausa)

def distribui_intervalo(intervalo_Total, N_tarefas):
    # Converte os horários das tarefas para float antes do cálculo
    horarios_tarefas_float = [Converte_Hora(tempo) for tempo in horarios_tarefas]
    
    # Distribui o intervalo proporcionalmente ao tempo de cada tarefa
    intervalo_parcial = [(tempo / horario_total_A) * intervalo_Total for tempo in horarios_tarefas_float]
    
    return intervalo_parcial  # Retorna em formato float para cálculos futuros

def Calcula_Intervalo_Interno(intervalo_Parcial_float , N_Intervalo_Interno):
    intervalo_interno = [ float(x) / N_Intervalo_Interno for x in intervalo_Parcial_float]
    return intervalo_interno

def float_para_hora(intervalo):
    def converter(valor):
        horas = int(valor)  # Parte inteira para horas
        minutos = int((valor - horas) * 60)  # Parte decimal para minutos
        return f"{horas:02d}:{minutos:02d}"

    if isinstance(intervalo, list):  # Verifica se intervalo é uma lista
        return [converter(valor) for valor in intervalo]
    else:  # Caso contrário, trata como um único valor
        return converter(intervalo)


# Início do código principal
N_tarefas = int(input("Digite quantas tarefas serão: "))

# Obter horários de início e fim
horario_começo = obter_entrada_hora("Digite que horas você deseja começar (H:M): ")
horario_fim = obter_entrada_hora("Digite que horas você deseja acabar (H:M): ")

#pausa
Pausa_str = input("digite quanto tempo de pausa vc quer entre as atividades(H:M): ")
Pausa = Converte_Hora(Pausa_str)
Pausa_float = Converte_Hora(Pausa_str)
Pausa_H = float_para_hora(Pausa)
#intervalo interno
N_Intervalo_Interno = int(input("digite quantos intervalos você quer durante as tarefas: "))

# Calcula e imprime a duração total
duração = Calcula_duracao(horario_começo.strftime("%H:%M"), horario_fim.strftime("%H:%M"))
duração_H = float_para_hora(duração)
print(f"Serão {duração_H} de duração.")
print("-" * 60)

horario_total_A = 0
horarios_tarefas = []
horario_total_A_H = float_para_hora(horario_total_A)

# Captura e exibe as tarefas, calculando intervalo em tempo real
for i in range(N_tarefas):
    print(f"Tarefa {i + 1}")
    tarefa, horas, importancia = Pega_Tarefa()
    print(f"Tarefa: {tarefa}")
    print(f"Tempo estimado: {float_para_hora(Converte_Hora(horas))}")
    print(f"Importância: {importancia}")
    print("-" * 60)
    
    horario_total_A += Converte_Hora(horas)  # Soma das horas das tarefas
    horarios_tarefas.append(horas)

# Agora que temos o horário total ocupado, podemos calcular o intervalo

if N_Intervalo_Interno != 0:

    intervalo_Total = Calcula_intervalo(horario_total_A, duração , Pausa)
    intervalo_Total_H = float_para_hora(intervalo_Total)

    intervalo_Parcial1 = distribui_intervalo(intervalo_Total, N_tarefas)
    intervalo_Parcial_float = intervalo_Parcial1  # Já é em float

    Intervalo_Interno = Calcula_Intervalo_Interno(intervalo_Parcial_float , N_Intervalo_Interno)
    print(f"Serão {duração_H} de duração, e você tem {horario_total_A_H} horas ocupadas.")
    print(f"Ou seja: {intervalo_Total_H} de intervalo.")
    print(f"A pausa entre as atividades é de: {Pausa_H}")
    print("-" * 60)

    # Aqui é onde o for deve estar
    for i in range(N_tarefas):
        intervalo_parcial_float = intervalo_Parcial1[i]
        intervalo_parcial_H = float_para_hora(intervalo_parcial_float)  # Converte para exibição
        
        intervalo_interno_float = Intervalo_Interno[i]
        intervalo_interno_H = float_para_hora(intervalo_interno_float)  # Converte para exibição
        
        print(f"Tarefa {i + 1}: {float_para_hora(Converte_Hora(horarios_tarefas[i]))} hora(s) de execução")
        print(f"Intervalo total para essa tarefa: {intervalo_parcial_H}")
        print(f"Serão {N_Intervalo_Interno} intervalo(s) de {intervalo_interno_H} cada")
        print("-" * 60)
else:
    print(f"Serão {duração_H} de duração, e você tem {horario_total_A_H} hora(s) ocupadas.")
    print("Seu cronograma não possui intervalos durante as atividades.")
    print(f"A pausa entre as atividades é de: {Pausa_H}")
    print("-" * 60)

    # Caso não haja intervalos internos
    for i in range(N_tarefas):
        print(f"Tarefa {i + 1}: {float_para_hora(Converte_Hora(horarios_tarefas[i]))} hora(s) de execução")
        print("-" * 60)

#tudo certo menos o horario_total_A_H
        