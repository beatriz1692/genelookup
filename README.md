# Gene Lookup - Python

Este projeto é um script em **Python** que permite ao usuário consultar genes humanos de forma interativa.  
Você pode digitar **uma sigla de gene** (ex.: `ADA`) ou **o nome completo do gene** (ex.: `adenosine deaminase`) e o programa retorna o **par correspondente** (sigla ↔ nome oficial).

O script utiliza a **API do HGNC (HUGO Gene Nomenclature Committee)** para obter informações oficiais sobre os genes.

---

## 🧩 Funcionalidades

- Consulta interativa de genes humanos.
- Suporte tanto para **siglas** quanto para **nomes completos**.
- Busca automática no banco oficial HGNC.
- Retorno do **nome oficial do gene** ou da **sigla**, dependendo do que foi digitado.
- Trata casos de ausência de informação, evitando erros.

---

## ⚡ Requisitos

- Python 3.7 ou superior
- Biblioteca `requests`

Instale a biblioteca `requests` com:

```bash
pip install requests
