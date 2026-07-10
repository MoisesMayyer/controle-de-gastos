import json
import os

def carregar_json():
    pass

def salvar_json(dados):
    pasta = "dados"
    arquivo = "dados/gastos.json"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(arquivo, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)
