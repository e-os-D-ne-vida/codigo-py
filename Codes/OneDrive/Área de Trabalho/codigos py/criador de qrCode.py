import os
import qrcode

# Link do site
url = "https://raphaelmota.pythonanywhere.com"

# Gerar o QR Code
qr = qrcode.QRCode(
    version=1,  # Tamanho do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Correção de erro
    box_size=10,  # Tamanho de cada quadrado
    border=4,  # Largura da borda
)
qr.add_data(url)
qr.make(fit=True)

# Criar a imagem do QR Code
img = qr.make_image(fill="black", back_color="white")

# Caminho para salvar a imagem
file_path = r"C:\Users\rapha\OneDrive\Área de Trabalho\pastas de qr code\meu_qrcode de datas.png"

# Salvar a imagem
img.save(file_path)

# Abrir a imagem com o visualizador de fotos padrão do Windows
os.startfile(file_path)
