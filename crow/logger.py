from datetime import datetime

LOG_FILE = "/logs/crow.log"


def registrar_log(mensagem):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    linha = f"[{timestamp}] {mensagem}\n"

    print(linha, end="", flush=True)

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(linha)


def ler_logs():

    try:

        with open(
            LOG_FILE,
            "r",
            encoding="utf-8"
        ) as arquivo:

            linhas = arquivo.readlines()

        return linhas[-100:]

    except FileNotFoundError:

        return []