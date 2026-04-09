"""
Santander Dev Week 2023 - Pipeline ETL com Python
===================================================
Como a API original foi descontinuada, os dados sao simulados localmente e o resultado é salvo em JSON.
"""

import json

# EXTRACT - Simulacao dos dados (substituindo o GET da API)

users = [
    {
        "id": 1,
        "name": "Pyterson",
        "account": {
            "id": 7,
            "number": "00001-1",
            "agency": "0001",
            "balance": 0.0,
            "limit": 500.0,
        },
        "card": {"id": 4, "number": "**** **** **** 1111", "limit": 1000.0},
        "features": [],
        "news": [],
    },
    {
        "id": 2,
        "name": "Pip",
        "account": {
            "id": 8,
            "number": "00002-2",
            "agency": "0001",
            "balance": 0.0,
            "limit": 500.0,
        },
        "card": {"id": 5, "number": "**** **** **** 2222", "limit": 1000.0},
        "features": [],
        "news": [],
    },
    {
        "id": 3,
        "name": "Pep",
        "account": {
            "id": 9,
            "number": "00003-3",
            "agency": "0001",
            "balance": 0.0,
            "limit": 500.0,
        },
        "card": {"id": 6, "number": "**** **** **** 3333", "limit": 1000.0},
        "features": [],
        "news": [],
    },
]

print("=== EXTRACT ===")
print(f"{len(users)} usuarios extraidos com sucesso!\n")


# TRANSFORM - Gera mensagens de marketing personalizadas
# Tirei a integração com a API pra subir no repositório público, então simulei o que a IA estava fazendo.

NEWS_ICON = "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg"


def generate_ai_news(user):

    messages = {
        "Pyterson": "Pyterson, invista hoje para garantir um futuro seguro e prospero. Seu futuro agradece!",
        "Pip": "Pip, investir eh o caminho para multiplicar seu dinheiro. Vamos fortalecer seu futuro financeiro!",
        "Pep": "Pep, investimentos sao a chave para o futuro financeiro. Cresca seu dinheiro, nao apenas o guarde!",
    }
    return messages.get(
        user["name"],
        f"{user['name']}, investir eh essencial para construir um futuro financeiro solido!",
    )


print("=== TRANSFORM ===")
for user in users:
    news = generate_ai_news(user)
    user["news"].append({"icon": NEWS_ICON, "description": news})
    print(f"  -> {user['name']}: {news}")

print()

# LOAD - Salva o resultado localmente (substituindo o PUT da API)

output_file = "users_updated.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print("=== LOAD ===")
for user in users:
    print(f"  User {user['name']} atualizado com sucesso!")

print(f"\nResultado salvo em '{output_file}'")
