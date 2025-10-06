import requests

def buscar_gene_interativo(entrada):
    entrada = entrada.strip()
    headers = {"Accept": "application/json"}

    # Primeiro tenta buscar como sigla
    url_sigla = f"https://rest.genenames.org/fetch/symbol/{entrada.upper()}"
    resposta = requests.get(url_sigla, headers=headers)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados["response"]["numFound"] > 0:
            gene = dados["response"]["docs"][0]
            symbol = gene.get("symbol", "N/A")
            name = gene.get("name") or gene.get("alias_name") or gene.get("prev_name", "N/A")
            return f"{symbol} → {name}"

    # Se não achou como sigla, tenta buscar como nome
    url_nome = f"https://rest.genenames.org/search/{entrada}"
    resposta = requests.get(url_nome, headers=headers)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados["response"]["numFound"] > 0:
            gene = dados["response"]["docs"][0]
            symbol = gene.get("symbol", "N/A")
            name = gene.get("name") or gene.get("alias_name") or gene.get("prev_name", "N/A")
            return f"{name} → {symbol}"

    return "Gene não encontrado."


# ------------------------
# Parte interativa
# ------------------------
if __name__ == "__main__":
    print("===== Gene Lookup =====")
    while True:
        entrada = input("Digite a sigla ou o nome do gene (ou 'sair' para encerrar): ").strip()
        if entrada.lower() == "sair":
            print("Encerrando programa.")
            break
        resultado = buscar_gene_interativo(entrada)
        print(resultado)
        print("-"*50)
