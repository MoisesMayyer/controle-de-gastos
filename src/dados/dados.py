import json
from pathlib import Path


CAMINHO_ARQUIVO = Path(__file__).parent / "gastos.json"


def carregar_json():

    if not CAMINHO_ARQUIVO.exists():
        return []

    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def salvar_json(dados):

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as file:
        json.dump(
            dados,
            file,
            indent=4,
            ensure_ascii=False
        )