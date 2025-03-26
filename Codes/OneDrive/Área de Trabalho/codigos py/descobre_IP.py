from scapy.all import ARP, Ether, srp
import time
import keyboard  # Biblioteca para capturar teclas
from plyer import notification

def scan_network(ip_range):
    print(f"Scanning network: {ip_range}")
    # Cria um pacote ARP
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Envia o pacote e recebe a resposta
    result = srp(packet, timeout=3, verbose=0)[0]

    # Lista de dispositivos encontrados
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # Substitua pelo intervalo de IP da sua rede
    Dispositivos_Vistos = []
    ignorar_Macs = ["cc:32:e5:e2:73:7e", "00:40:a7:2f:eb:9f"]  # MACs que devem ser ignorados

    print("Pressione 'x' para sair do programa.")
    try:
        while True:
            if keyboard.is_pressed("x"):  # Verifica se a tecla 'x' foi pressionada
                print("\nPrograma interrompido pelo usuário.")
                break

            devices = scan_network(ip_range)

            # Verifica se nenhum dispositivo foi encontrado
            if not devices:
                if Dispositivos_Vistos:  # Limpa dispositivos anteriores e notifica
                    print("\rNenhum aparelho encontrado! Lista limpa.", flush=True)
                    Dispositivos_Vistos.clear()
                else:
                    print("\rNenhum aparelho encontrado", flush=True)
            else:
                Nome_Repetido = []
                for device in devices:
                    if device['mac'] in ignorar_Macs:
                        continue  # Ignora dispositivos com MACs na lista de ignorados
                    
                    if device in Dispositivos_Vistos:
                        Nome_Repetido.append(device)
                    else:
                        Dispositivos_Vistos.append(device)
                        print(f"Novo dispositivo: IP: {device['ip']} - MAC: {device['mac']}")
                
                # Notifica dispositivos repetidos
                if Nome_Repetido:
                    print("\nDispositivos repetidos encontrados:")
                    for repetido in Nome_Repetido:
                        print(f"IP: {repetido['ip']} - MAC: {repetido['mac']}")
                    notification.notify(
                        title="Notificação de Alerta",
                        message=f"Dispositivos IP: {repetido['ip']} - MAC: {repetido['mac']} repetidos encontrados!",
                        timeout=5  # Tempo (em segundos) que a notificação será exibida
                    )

            time.sleep(5)  # Espera 5 segundos antes de realizar a próxima varredura
    except Exception as e:
        print(f"\nErro: {e}")



