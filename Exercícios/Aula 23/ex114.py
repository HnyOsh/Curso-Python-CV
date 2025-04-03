import requests

try:
    site = requests.get("https://www.youtube.com")
except requests.exceptions.RequestException:
    print(f'Não consegui acessar o site')
else:
    print(f'Site acessado com sucesso')

