from flask import (Flask,render_template,jsonify,request)

from docker_manager import listar_containers

from config_manager import (carregar_imagens,adicionar_imagem,remover_imagem)

from runtime_manager import (carregar_runtime,salvar_runtime)


from logger import ler_logs



app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def index():

    return render_template(
        "index.html"
    )


@app.route("/api/containers")
def api_containers():

    return jsonify(
        listar_containers()
    )


@app.route("/api/images")
def api_images():

    return jsonify(
        carregar_imagens()
    )


@app.route("/api/images", methods=["POST"])
def api_add_image():

    dados = request.get_json()

    imagem = dados.get(
        "imagem",
        ""
    ).strip()

    if not imagem:

        return jsonify({
            "sucesso": False
        }), 400

    sucesso = adicionar_imagem(
        imagem
    )

    return jsonify({
        "sucesso": sucesso
    })


@app.route(
    "/api/images/<path:imagem>",
    methods=["DELETE"]
)
def api_delete_image(imagem):

    sucesso = remover_imagem(
        imagem
    )

    return jsonify({
        "sucesso": sucesso
    })


@app.route("/api/logs")
def api_logs():

    return jsonify(
        ler_logs()
    )

@app.route("/api/runtime")
def api_runtime():

    return jsonify(
        carregar_runtime()
    )


@app.route(
    "/api/runtime",
    methods=["POST"]
)
def api_update_runtime():

    dados = request.get_json()

    monitorando = dados.get(
        "monitorando",
        False
    )

    intervalo = int(
        dados.get(
            "intervalo",
            30
        )
    )

    salvar_runtime(
        monitorando,
        intervalo
    )

    return jsonify({
        "sucesso": True
    })