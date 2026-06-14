import docker

from config import CONTAINERS_PROTEGIDOS

client = docker.from_env()


def listar_containers():

    containers_info = []

    for container in client.containers.list(all=True):

        containers_info.append({
            "nome": container.name,
            "status": container.status,
            "tags": container.image.tags,
            "image_id": container.image.id
        })

    return containers_info


def obter_container(nome):

    try:
        return client.containers.get(nome)

    except docker.errors.NotFound:
        return None


def obter_config_recriacao(nome):

    container = obter_container(nome)

    if not container:
        return None

    return {
        "nome": container.name,
        "imagem": (
            container.image.tags[0]
            if container.image.tags
            else None
        ),
        "env": container.attrs["Config"]["Env"],
        "command": container.attrs["Config"]["Cmd"],
        "restart_policy": container.attrs["HostConfig"]["RestartPolicy"]
    }


def buscar_containers_por_imagem(imagem):

    encontrados = []

    for container in client.containers.list(all=True):

        if imagem in container.image.tags:

            encontrados.append({
                "nome": container.name,
                "status": container.status,
                "tags": container.image.tags,
                "image_id": container.image.id
            })

    return encontrados


def parar_container(nome):

    if nome in CONTAINERS_PROTEGIDOS:
        print(f"[PROTEGIDO] {nome}")
        return False

    container = obter_container(nome)

    if not container:
        return False

    print(f"Parando {nome}")

    container.stop()

    return True


def remover_container(nome):

    if nome in CONTAINERS_PROTEGIDOS:
        print(f"[PROTEGIDO] {nome}")
        return False

    container = obter_container(nome)

    if not container:
        return False

    print(f"Removendo {nome}")

    container.remove()

    return True


def criar_container(config):

    print(f"Criando {config['nome']}")

    return client.containers.run(
        image=config["imagem"],
        name=config["nome"],
        detach=True,
        environment=config["env"],
        command=config["command"],
        restart_policy=config["restart_policy"]
    )

def listar_containers_monitorados():

    containers = []

    for container in client.containers.list(all=True):

        containers.append({
            "nome": container.name,
            "status": container.status,
            "imagem": (
                container.image.tags[0]
                if container.image.tags
                else "sem-tag"
            )
        })

    return containers