import schedule
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def executar_script():
    # Configuração do ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/rapha/AppData/Local/Google/Chrome/User Data")
    service = Service("C:/Users/rapha/Desktop/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    # Abre o WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Espera até que o WhatsApp Web carregue completamente
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))

    def enviar_mensagem(contato, mensagens):
        try:
            # Busca o contato corretamente
            search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))
            search_box.clear()
            search_box.send_keys(contato)
            time.sleep(random.uniform(2, 5))  # Tempo aleatório entre 2 e 5 segundos
            search_box.send_keys(Keys.ENTER)
            time.sleep(random.uniform(3, 6))  # Tempo aleatório entre 3 e 6 segundos

            # Busca a caixa de mensagem correta
            chat_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")))

            for mensagem in mensagens:
                chat_box.send_keys(mensagem)
                time.sleep(random.uniform(1, 2))  # Pequena pausa entre mensagens no mesmo contato
                chat_box.send_keys(Keys.ENTER)
                time.sleep(random.uniform(1, 2))  # Pequena pausa para evitar envio rápido demais

            print(f"✅ Mensagens enviadas para {contato}")

        except Exception as e:
            print(f"❌ Erro ao enviar mensagem para {contato}: {e}")

    # Função agendada para enviar mensagens para cada contato
    def enviar_mensagens_agendadas():
        contatos = ["xd", "Mano Kuririn", "Rafael Ferreira", "Elias", "Henrique Qi Qi", "micro SD ⚜️", "π8"]
        mensagens = [
            "hey hey",
            "vai querer algum lanche pra amanhã?",
        ]
        
        for contato in contatos:
            enviar_mensagem(contato, mensagens)
            tempo_espera = random.uniform(10, 30)  # Tempo aleatório entre 10 e 30 segundos apenas entre contatos
            print(f"⏳ Aguardando {tempo_espera:.2f} segundos antes de enviar para o próximo contato...")
            time.sleep(tempo_espera)

    # Executa a função para enviar as mensagens
    enviar_mensagens_agendadas()

    # Fecha o navegador após o envio das mensagens
    driver.quit()

# Agendar para rodar o script completo em um horário específico, por exemplo, às 21:00
schedule.every().day.at("21:00").do(executar_script)

# Também é possível rodar o script de imediato para testes
executar_script()

# Loop para rodar o agendador
# while True:
#     schedule.run_pending()
#     time.sleep(1)
