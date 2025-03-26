import requests
import platform

# Obtém os dados JSON do CfT
json_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json"
response = requests.get(json_url)
data = response.json()

# Escolhe o canal Stable
stable_info = data.get("channels", {}).get("Stable", {})
version = stable_info.get("version")
print("Versão Stable:", version)

# Determina a plataforma e o nome do diretório/arquivo
sistema = platform.system().lower()
if sistema == "windows":
    pasta = "win64"  # Para Windows o diretório correto é "win64"
    arquivo = "chromedriver-win64.zip"
elif sistema == "darwin":
    pasta = "mac-x64"
    arquivo = "chromedriver-mac-x64.zip"
else:
    pasta = "linux64"
    arquivo = "chromedriver-linux64.zip"

# Monta a URL para download
download_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/{pasta}/{arquivo}"
print("URL de download:", download_url)

# Para fazer o download automatizado:
download_response = requests.get(download_url)
if download_response.status_code == 200:
    with open(arquivo, "wb") as f:
        f.write(download_response.content)
    print("Download concluído!")
else:
    print("Erro no download:", download_response.status_code)
