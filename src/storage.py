
import json
from pathlib import Path

# Arquivo onde os dados do sistema serão armazenados.
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "f1_data.json"


def salvar_dados(corridas, pilotos, equipes, resultados):
    """Salva os dados do sistema em um arquivo JSON."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    dados = {
        "corridas": corridas,
        "pilotos": pilotos,
        "equipes": equipes,
        "resultados": resultados,
    }

    with DATA_FILE.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def carregar_dados():
    """Carrega os dados salvos ou retorna listas vazias."""
    if not DATA_FILE.exists():
        return [], [], [], []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return (
            dados.get("corridas", []),
            dados.get("pilotos", []),
            dados.get("equipes", []),
            dados.get("resultados", []),
        )
    except (json.JSONDecodeError, OSError):
        print("Aviso: não foi possível carregar os dados salvos.")
        return [], [], [], []
