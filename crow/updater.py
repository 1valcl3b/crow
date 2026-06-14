from docker_manager import (
    obter_config_recriacao,
    buscar_containers_por_imagem,
    parar_container,
    remover_container,
    criar_container
)

from image_manager import verificar_atualizacao

from logger import registrar_log


def atualizar_container(nome):

    registrar_log(
        f"Iniciando atualização do container {nome}"
    )

    config = obter_config_recriacao(nome)

    if not config:

        registrar_log(
            f"Configuração não encontrada para {nome}"
        )

        return

    registrar_log(
        f"Parando container {nome}"
    )

    parar_container(nome)

    registrar_log(
        f"Removendo container {nome}"
    )

    remover_container(nome)

    registrar_log(
        f"Recriando container {nome}"
    )

    criar_container(config)

    registrar_log(
        f"Container {nome} atualizado com sucesso"
    )


def atualizar_imagem(imagem):

    registrar_log(
        f"Verificando imagem {imagem}"
    )

    resultado = verificar_atualizacao(imagem)

    if not resultado["mudou"]:

        registrar_log(
            f"Nenhuma atualização encontrada para {imagem}"
        )

        return

    registrar_log(
        f"Nova versão detectada para {imagem}"
    )

    containers = buscar_containers_por_imagem(imagem)

    if not containers:

        registrar_log(
            f"Nenhum container encontrado utilizando {imagem}"
        )

        return

    for container in containers:

        atualizar_container(
            container["nome"]
        )