import tkinter as tk

Numero1 = None
Numero2 = None
Numero3 = None

def Automatizar_Entrada(event):
    global Numero1, Numero2, Numero3

    EntradaAutomatica = int(Vlinha.get())
    print(f"o valor da linha eh {EntradaAutomatica}")
    if EntradaAutomatica == 2:
        Numero1 = tk.Entry(tela, 
                           font=('None', 25, 'bold'), 
                           fg='darkgreen', 
                           width=12,
                           bg='black',
                           justify='center')
        Numero1.place(x=500, y=200)
        
        Numero2 = tk.Entry(tela, 
                           font=('None', 25, 'bold'), 
                           fg='darkgreen', 
                           width=12,
                           bg='black', 
                           justify='center')
        Numero2.place(x=500, y=300)
    elif EntradaAutomatica == 3:

        Numero1 = tk.Entry(tela, 
                           font=('None', 20, 'bold'), 
                           fg='darkgreen', 
                           width=14,
                           bg='black',
                           justify='center')
        Numero1.place(x=480, y=200)
        Numero2 = tk.Entry(tela, 
                           font=('None', 20, 'bold'), 
                           fg='darkgreen', 
                           width=14,
                           bg='black', 
                           justify='center')
        Numero2.place(x=480, y=300)
        Numero3 = tk.Entry(tela, 
                           font=('None', 20, 'bold'), 
                           fg='darkgreen', 
                           width=14, 
                           bg='black', 
                           justify='center')
        Numero3.place(x=480, y=400)

matriz = []  # espaço vazio para armazenar a matriz

def automatizaçao(equation):
    # Remove espaços desnecessários
    equation = equation.replace(' ', '')
    
    # Divide a equação na parte da esquerda e na parte do resultado
    L_esquerdo, L_direito = equation.split('=')
    L_direito = float(L_direito)
    
    # Inicializa os coeficientes de x, y e z
    a = b = c = 0
    
    # Separa os termos da equação
    terms = []
    term = ''
    for char in L_esquerdo:
        if char in '+-' and term:
            terms.append(term)
            term = char
        else:
            term += char
    terms.append(term)
    
    # Processa os termos para extrair os coeficientes
    for term in terms:
        if 'x' in term:
            coefficient = term.replace('x', '')
            a = float(coefficient) if coefficient not in ['', '+'] else 1.0
            a = -1.0 if coefficient == '-' else a
        elif 'y' in term:
            coefficient = term.replace('y', '')
            b = float(coefficient) if coefficient not in ['', '+'] else 1.0
            b = -1.0 if coefficient == '-' else b
        elif 'z' in term:
            coefficient = term.replace('z', '')
            c = float(coefficient) if coefficient not in ['', '+'] else 1.0
            c = -1.0 if coefficient == '-' else c
    
    return a, b, c, L_direito  # Retorna os coeficientes e o lado direito da equação

def CalculaSistema():
    try:
        ValorVlinha = int(Vlinha.get())  # Pega o valor de Vlinha
        
        if ValorVlinha == 2:
            # Pega as equações dos campos de entrada
            equacao_str1 = Numero1.get()
            equacao_str2 = Numero2.get()
            
            # Processa ambas as equações
            a1, b1, c1, L_direito1 = automatizaçao(equacao_str1)
            a2, b2, c2, L_direito2 = automatizaçao(equacao_str2)
            
            # Cria a matriz a partir dos coeficientes e termos independentes
            matriz = [
                [a1, b1, L_direito1],
                [a2, b2, L_direito2]
            ]
            
            # Atribui os valores da matriz a variáveis separadas
            j, k, l, m = matriz[0][0], matriz[0][1], matriz[1][0], matriz[1][1]
            
            # Calcula o determinante comum
            determinanteC = (j * m) - (k * l)
            print(determinanteC)

            if determinanteC == 0.0:
                print("Não existe determinante possível")
            else:
                # Calcula os determinantes para X e Y
                determinanteX = (L_direito1 * m) - (k * L_direito2)
                determinanteY = (j * L_direito2) - (l * L_direito1)
                valor_X = determinanteX / determinanteC
                valor_Y = determinanteY / determinanteC
                print(f"determinate x {determinanteX} e o determinantey {determinanteY}")
                print(f"O valor da primeira incógnita é = {valor_X}\nO valor da segunda incógnita é = {valor_Y}")
            
            resultado_label.config(text=f"O valor de x eh {valor_X} \nO valor de y eh {valor_Y}")
        
        # Aqui você pode adicionar um caso para o valor diferente de 2, se necessário
        else:
            equacao_str1 = Numero1.get()
            equacao_str2 = Numero2.get()
            equacao_str3 = Numero3.get()

     # Processa as equações
            a1, b1, c1, L_direito1 = automatizaçao(equacao_str1)
            a2, b2, c2, L_direito2 = automatizaçao(equacao_str2)
            a3, b3, c3, L_direito3 = automatizaçao(equacao_str3)

            matriz = [
           [a1, b1, c1, L_direito1],
           [a2, b2, c2, L_direito2],
           [a3, b3, c3, L_direito3]
         ]

            a, b, c = matriz[0][0], matriz[0][1], matriz[0][2]
            d, e, f = matriz[1][0], matriz[1][1], matriz[1][2]
            g, h, i = matriz[2][0], matriz[2][1], matriz[2][2]

     # Cálculo do determinante
            determinanteC = (
            (a * e * i) + (b * f * g) + (c * d * h)
             - (c * e * g) - (b * d * i) - (a * f * h)
             )
            print(f"O determinante comum é {determinanteC}")
            if determinanteC == 0.0:
             print("Não existe determinante possível")
             resultado_label.config(text=("não existe determinante \n comum"))
            else:
        # Calcula os determinantes para X, Y e Z
             determinanteX = (
               (L_direito1 * e * i) + (b * f * L_direito3) + (c * L_direito2 * h)
              - (c * e * L_direito3) - (L_direito1 * f * h) - (b * L_direito2 * i)
                    )
             determinanteY = (
              (a * L_direito2 * i) + (L_direito1 * f * g) + (c * d * L_direito3)
              - (c * L_direito2 * g) - (a * f * L_direito3) - (L_direito1 * d * i)
             )
             determinanteZ = (
              (a * e * L_direito3) + (b * L_direito2 * g) + (L_direito1 * d * h)
              - (L_direito1 * e * g) - (a * L_direito2 * h) - (b * d * L_direito3)
             )

             valor_X = determinanteX / determinanteC
             valor_Y = determinanteY / determinanteC
             valor_Z = determinanteZ / determinanteC

             print(
             f"o determinante x eh {determinanteX} , o determinante Y eh {determinanteY}, o determinante z eh {determinanteZ}"
             f"O valor da primeira incógnita é = {valor_X}\n"
             f"O valor da segunda incógnita é = {valor_Y}\n"
             f"O valor da terceira incógnita é = {valor_Z}\n"
             )

             resultado_label.config(
             text=(
                f"O valor de x é {valor_X}\n"
                f"O valor de y é {valor_Y}\n"
                f"O valor de z é {valor_Z}  "
              )
             )

    except ValueError:
        resultado_label.config(
            text=("insira valores válidos")
        )
#obs: não pode colocar letra maiuscula, apenas x , y e z e não X,Y,Z
tela = tk.Tk()#criando a janela
tela.title('testando')#titulo da janela
tela.geometry ('1180x720')#formatação largura x altura
tela.config(bg= 'white')# deixa a tela toda preta

Calcular = tk.Button(tela, 
                fg= 'darkgreen', 
                bg= 'black' ,
                height= 3,
                width= 8,
                text= "Calcular" ,
                font=('None', 15, 'bold') ,
                command= CalculaSistema)
Calcular.place(x= 940 , y= 200)
    
Qlinha= tk.Label(tela, font=('None', 15, 'bold' ) , 
                fg= 'white', 
                bg= 'black' ,
                text= (f"  coloque o numero de linhas(2 ou 3)") ,
                height= 2 ,
                width= 20,
                wraplength= 200 )
Qlinha.place(x= 880, y = 340)

Vlinha = tk.Entry(tela, 
                font=('None', 25, 'bold' ) , 
                fg= 'white', 
                width = 10 ,
                bg= 'black' ,
                justify= 'center' )
Vlinha.place(x=900, y= 400)
Vlinha.bind("<Return>" , Automatizar_Entrada) # sempre que a tecla return é pressionada o dado é printado

resultado_label = tk.Label(tela, font=('None', 20, 'bold'), fg='darkgreen', bg='black')
resultado_label.place(x=450, y= 550)

texto = tk.Label(tela,
                text= ' Testando' ,   # configurações de texto como o título
                font= ('None', 40, 'bold' ) , # configuração de fonte,tamanho e tipo (font= ("fonte" , tamanho , tipo))
                fg= 'white', # cor do texto
                bg= 'black' ) # cor do fundo do texto
texto.place(x=450, y=10)



tela.mainloop() # encerrar a janela
