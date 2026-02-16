import requests
import csv

def buscar_personagens():
    personagens = []

    # Vamos buscar 3 páginas (cada página tem 20 personagens)
    for page in range(1, 4):
        url = f"https://rickandmortyapi.com/api/character?page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            personagens.extend(data["results"])
        else:
            print("Erro ao acessar API")
            return []

    # Retorna apenas os primeiros 50
    return personagens[:50]


def gerar_csv(personagens):
    with open("characters.csv", mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")

        # Cabeçalho
        writer.writerow(["id", "name", "status", "species", "type", "gender"])

        # Dados
        for p in personagens:
            writer.writerow([
                p["id"],
                p["name"],
                p["status"],
                p["species"],
                p["type"],
                p["gender"]
            ])

    print("Arquivo characters.csv criado com sucesso!")


def main():
    personagens = buscar_personagens()

    if personagens:
        gerar_csv(personagens)
    else:
        print("Nenhum personagem encontrado.")


if __name__ == "__main__":
    main()
