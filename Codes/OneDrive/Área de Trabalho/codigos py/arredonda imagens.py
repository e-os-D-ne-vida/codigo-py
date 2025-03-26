from PIL import Image, ImageDraw, ImageFilter

# Abrir a imagem
imagem = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\Sonia_Moda_jeans\static\images\boné.jpg")

# Criar uma máscara com bordas arredondadas
largura, altura = imagem.size
mascara = Image.new("L", (largura, altura), 0)
desenhando = ImageDraw.Draw(mascara)
raio = 120  # Raio do arredondamento das bordas
desenhando.rounded_rectangle([0, 0, largura, altura], raio, fill=255)
# para a camisa o raio foi 200 , para a calça foi 120
# Aplicar a máscara à imagem
imagem_com_bordas_arredondadas = imagem.convert("RGBA")
imagem_com_bordas_arredondadas.putalpha(mascara)

# Salvar a imagem resultante
imagem_com_bordas_arredondadas.save(r"C:\Users\rapha\OneDrive\Área de Trabalho\Sonia_Moda_jeans\static\images\boné_desenho.png")

