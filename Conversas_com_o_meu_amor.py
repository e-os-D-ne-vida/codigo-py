import os
import re

# Nome dos arquivos
arquivo = r"C:\Users\rapha\Desktop\Conversas_com_Ela.txt" # Arquivo original
Novo_arquivo = "Conversas_Fael_2025.txt"  # Arquivo para armazenar mensagens de 2025

# Expressão regular para capturar a data no formato DD/MM/YYYY HH:MM
data_regex = r'^\d{2}/\d{2}/(\d{4}) \d{2}:\d{2} - '

def limpar_texto(texto):
    texto = re.sub(r'<Mídia oculta>', '', texto)
    texto = texto.replace('null', '')
    texto = re.sub(r'\s+', ' ', texto)  # Reduz múltiplos espaços para um único
    texto = re.sub(r'[^\w\sÀ-ÿ\.\,\!\?\;\:\(\)\-]', '', texto, flags=re.UNICODE)
    return texto.strip()

def extrair_mensagens_fael():
    """Lê o arquivo original, filtra mensagens do Fael de 2025 e escreve no novo arquivo em ordem cronológica."""
    if not os.path.exists(arquivo):
        print(f"O arquivo {arquivo} não existe.")
        return

    mensagens_fael_2025 = []  # Lista para armazenar mensagens de 2025
    primeira_data = None  # Variável para armazenar a primeira data encontrada
    ultima_data = None  # Variável para armazenar a última data encontrada

    # Verifica se o arquivo já existe e carrega as mensagens para evitar duplicatas
    mensagens_ja_existentes = set()
    if os.path.exists(Novo_arquivo):
        with open(Novo_arquivo, "r", encoding="utf-8") as f2:
            mensagens_ja_existentes = set(f2.read().splitlines())

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            # Encontrar a data na linha
            match = re.match(data_regex, linha)
            if match:
                ano = match.group(1)  # Captura o ano da data
                data_atual = linha.split(' - ')[0]  # Captura a data atual da linha
                linha = re.sub(data_regex, '', linha).strip()  # Remove a data da linha

                # Verifica se o ano é 2025
                if ano == '2025':
                    # Atualiza a primeira data se ainda não foi definida
                    if primeira_data is None:
                        primeira_data = data_atual
                    
                    ultima_data = data_atual  # Atualiza a última data encontrada

                    # Verifica se a linha contém "Fael:" após a remoção da data
                    if "Fael: " in linha:
                        mensagem = linha.split("Fael: ", 1)[-1].strip()
                        mensagem_limpa = limpar_texto(mensagem)

                        if mensagem_limpa and mensagem_limpa not in mensagens_ja_existentes:
                            mensagens_fael_2025.append(mensagem_limpa)  # Adiciona à lista

    # Escreve as mensagens filtradas no novo arquivo em ordem cronológica
    if mensagens_fael_2025:
        with open(Novo_arquivo, "a", encoding="utf-8") as f2:
            for mensagem in mensagens_fael_2025:
                f2.write(mensagem + "\n")

        print(f"Mensagens de Fael de 2025 foram extraídas para {Novo_arquivo}.")

    # Exibe a primeira e a última data encontrada no terminal (sem salvar no arquivo)
    if primeira_data and ultima_data:
        print(f"📅 Primeira mensagem registrada em: {primeira_data}")
        print(f"📅 Última mensagem registrada em: {ultima_data}")
    else:
        print("Nenhuma mensagem de 2025 encontrada.")

# Executa a função
extrair_mensagens_fael()
