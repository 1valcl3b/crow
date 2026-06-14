import json

ARQUIVO_CONFIG = "/config/images.json"


def carregar_imagens():

    try:

        with open(
            ARQUIVO_CONFIG,
            "r",
            encoding="utf-8"
        ) as arquivo:

            dados = json.load(arquivo)

            return dados.get(
                "imagens",
                []
            )

    except Exception as e:

        print(
            f"Erro ao carregar configuração: {e}"
        )

        return []


def salvar_imagens(imagens):

    dados = {
        "imagens": imagens
    }

    with open(
        ARQUIVO_CONFIG,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            dados,
            arquivo,
            indent=4
        )


def adicionar_imagem(imagem):

    imagens = carregar_imagens()

    if imagem not in imagens:

        imagens.append(imagem)

        salvar_imagens(imagens)

        return True

    return False


def remover_imagem(imagem):

    imagens = carregar_imagens()

    if imagem in imagens:

        imagens.remove(imagem)

        salvar_imagens(imagens)

        return True

    return False