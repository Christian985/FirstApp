import requests


def exemplo_cep():
    cep = "16702144"

    url = f"https://viacesp.com.br/ws/{cep}/json/"
    response = requests.get(url)

    # Caso tenha sucesso, armazena a informação
    if response.status_code == 200:
        dados_cep = response.json()
        # Usar '' dentro de "" para não dar erro
        print(f"Logradouro: {dados_cep['Logradouro']}")
    else:
        print(f"Erro: {response.status_code}")


def exemplo_get(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)

    if response.status_code == 200:
        dados_get_postagem = response.json()

        print(f"Título: {dados_get_postagem['title']}\n")
        print(f"Conteúdo: {dados_get_postagem['body']}")
    else:
        print(f"Erro: {response.status_code}")


# exemplo_get(5)


# Somente o put usa 201
def exemplo_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    nova_postagem = {
        "title": "Novo titulo",
        "body": "Novo conteudo",
        "userID": 1
    }

    response = requests.post(url, json=nova_postagem)

    if response.status_code == 201:
        dados_postagem = response.json()
        print(f"Titulo: {dados_postagem['title']}\n")
        print(f"Conteúdo: {dados_postagem['body']}")
    else:
        print(f"Erro: {response.status_code}")


# exemplo_post()


def exemplo_put(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    nova_postagem = {
        "id": id,
        "title": "Novo titulo",
        "body": "Novo conteudo",
        "userID": 1
    }
    antes = requests.get(url)
    response = requests.put(url, json=nova_postagem)

    if response.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f"Titulo Asntigo: {dados_antes['title']}\n")
        else:
            print(f"Erro: {response.status_code}")
        dados_postagem = response.json()
        print(f"Titulo: {dados_postagem['title']}\n")
    else:
        print(f"Erro: {response.status_code}")


exemplo_put(1)
