import requests

cep = "01001000"

url = f"https://viacesp.com.br/ws/{cep}/json/"
response = requests.get(url)

# Caso tenha sucesso, armazena a informação
if response.status_code == 200:
    dados_cep = response.json()
    # Usar '' dentro de "" para não dar erro!
    print(f"Logradouro: {dados_cep['Logradouro']}")
else:
    print(f"Erro: {response.status_code}")