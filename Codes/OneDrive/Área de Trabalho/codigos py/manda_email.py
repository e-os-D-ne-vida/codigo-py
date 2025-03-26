import smtplib
import time
from plyer import notification

Vezes = 5
Enviado = 0
tempo = 10 

def mandar_email(destino , assunto , mensagem):
    remetente = "raphaelcatanduba7115@gmail.com"
    senha = "fgcb eaqk dirk zatj"
    servidor_smtp = "smtp.gmail.com"
    porta = 587

    try:
        server = smtplib.SMTP(servidor_smtp, porta)
        server.starttls()
        server.login(remetente, senha)

        mensagem_formatada = f"Subject: {assunto}\n\n{mensagem}".encode("utf-8")

        server.sendmail(remetente,destino, mensagem_formatada)
        print("Email enviado com sucesso")

        
    except Exception as e:
        print("Erro ao enviar email" , e)
        notification.notify (
            title="Erro ao enviar email",
            message="Erro no envio do email",
            timeout=tempo
          )
        
    finally:
        server.quit()

#enviando_email = (f"{destino} , {assunto} , {mensagem}")
destino = "raphaelcatanduba7115@gmail.com"
mensagem = "oii amor, tô mandando email pelo python dnv, é só pra vc não esquecer que eu te amo e to com saudades\n obs: vou enviar isso automáticamente 5 vezes e quero que cada vez vc me responda pelo whatsapp, de preferencia com uma fotinho sua pra eu ficar feliz, aproveita amor\n talvez os proximos caiam como spam"  

while Vezes > Enviado:
    Enviado += 1
    assunto = f"{Enviado}º email para o meu amor"
    mandar_email(destino, assunto, mensagem)

    notification.notify( 
    title = f"Email {Enviado} enviado com sucesso", 
    message = "Os emails foram enviados com sucesso, verifique sua caixa de entrada", 
    timeout = tempo
) 

    print(f"Email {Enviado } enviado")

    time.sleep(tempo)  # Espera 1 minuto para enviar o próximo email

notification.notify( 
    title = "Email enviado com sucesso", 
    message = "Os emails foram enviados com sucesso, verifique sua caixa de entrada", 
    timeout = 10
)