import pandas as pd
import re
import pywhatkit as kit

# Lista de produtos disponíveis
produtos_disponiveis = ["pão de queijo", "café", "bolo", "suco", "coxinha", "enroladinho", "joelho"]

# Função para extrair dados da mensagem
def extrair_dados(mensagem):
    # Ajusta a regex para pegar qualquer remetente (nome pode ter espaço ou ser único)
    match = re.search(r"\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}\]\s*([A-Za-z\s]+):\s*([\w\s]+):\s*(.+)", mensagem, re.IGNORECASE)
    
    if not match:
        return None, None, None, mensagem.strip()

    nome = match.group(2).strip()  # Nome da pessoa que fez o pedido
    texto_pedido = match.group(3).lower().strip()  # Mensagem do pedido

    produto_encontrado = None
    quantidade = 1  # Assume 1 unidade por padrão

    # Verifica se algum produto está na mensagem
    for produto in produtos_disponiveis:
        if produto in texto_pedido:
            produto_encontrado = produto
            break

    # Se encontrou um produto, verifica se tem número antes
    if produto_encontrado:
        match_qtd = re.search(r"(\d+)\s*" + produto_encontrado, texto_pedido)
        if match_qtd:
            quantidade = int(match_qtd.group(1))  # Define a quantidade correta

    return nome, produto_encontrado, quantidade, mensagem.strip()

# Ler o arquivo do chat
with open(r"C:\Users\rapha\Desktop\Codes\chat.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# Criar lista de dados extraídos
dados = []
for i, linha in enumerate(linhas, start=1):
    nome, produto, quantidade, mensagem_original = extrair_dados(linha)
    if nome and produto:
        dados.append([i, nome, produto, quantidade, mensagem_original])

# Criar DataFrame (tabela)
df = pd.DataFrame(dados, columns=["ID", "Nome", "Produto", "Quantidade", "Mensagem"])

# Exibir a tabela
print(df.to_string())

# Salvar os dados
df.to_csv("tabela_pedidos.csv", index=False)
#df.to_excel("tabela_pedidos.xlsx", index=False)

numero = "+5521978935622"  # Substitua pelo número com DDD
arquivo = "tabela_pedidos.csv"

# Enviar pelo WhatsApp (se necessário)
#kit.sendwhats_document(numero, arquivo)
