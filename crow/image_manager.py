import docker

from config import FORCAR_ATUALIZACAO

client = docker.from_env()


def obter_image_id(imagem):

    try:
        image = client.images.get(imagem)
        return image.id

    except docker.errors.ImageNotFound:
        return None


def pull_imagem(imagem):

    return client.images.pull(imagem)


def verificar_atualizacao(imagem):

    image_antiga = obter_image_id(imagem)

    pull_imagem(imagem)

    image_nova = obter_image_id(imagem)

    mudou = image_antiga != image_nova

    if FORCAR_ATUALIZACAO:
        mudou = True

    return {
        "imagem": imagem,
        "antes": image_antiga,
        "depois": image_nova,
        "mudou": mudou
    }