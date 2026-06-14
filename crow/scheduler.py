import time

from updater import atualizar_imagem

from config_manager import carregar_imagens

from runtime_manager import carregar_runtime

from logger import registrar_log


def iniciar_scheduler():

    while True:

        runtime = carregar_runtime()

        monitorando = runtime.get(
            "monitorando",
            False
        )

        intervalo = runtime.get(
            "intervalo",
            30
        )

        if not monitorando:

            time.sleep(1)

            continue

        registrar_log(
            "Iniciando nova verificação"
        )

        imagens = carregar_imagens()

        for imagem in imagens:

            try:

                atualizar_imagem(
                    imagem
                )

            except Exception as e:

                registrar_log(
                    f"Erro: {e}"
                )

        time.sleep(intervalo)