import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

if __name__ == "__main__":
    public_ip = get_public_ip()
    print(f"Public IP: {public_ip}")
