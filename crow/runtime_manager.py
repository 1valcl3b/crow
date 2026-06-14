import json

ARQUIVO_RUNTIME = "/config/runtime.json"


def carregar_runtime():

    try:

        with open(
            ARQUIVO_RUNTIME,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    except:

        return {
            "monitorando": False,
            "intervalo": 30
        }


def salvar_runtime(
    monitorando,
    intervalo
):

    dados = {
        "monitorando": monitorando,
        "intervalo": intervalo
    }

    with open(
        ARQUIVO_RUNTIME,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            dados,
            arquivo,
            indent=4
        )