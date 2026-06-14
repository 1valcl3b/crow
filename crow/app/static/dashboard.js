async function carregarContainers() {

    const resposta =
        await fetch("/api/containers");

    const containers =
        await resposta.json();

    const tbody =
        document.querySelector(
            "#containers-table tbody"
        );

    tbody.innerHTML = "";

    containers.forEach(container => {

        let imagem = "sem-tag";

        if (
            container.tags &&
            container.tags.length > 0
        ) {
            imagem = container.tags[0];
        }

        tbody.innerHTML += `
            <tr>
                <td>${container.nome}</td>
                <td>${container.status}</td>
                <td>${imagem}</td>
            </tr>
        `;
    });
}


async function carregarImagens() {

    const resposta =
        await fetch("/api/images");

    const imagens =
        await resposta.json();

    const lista =
        document.getElementById(
            "images-list"
        );

    lista.innerHTML = "";

    imagens.forEach(imagem => {

        lista.innerHTML += `
            <li>
                ${imagem}
                <button
                    onclick="removerImagem('${imagem}')"
                >
                    Remover
                </button>
            </li>
        `;
    });
}


async function atualizarDashboard() {

    await carregarContainers();

    await carregarImagens();

    await carregarLogs();

    await carregarRuntime();
}


atualizarDashboard();

setInterval(
    atualizarDashboard,
    5000
);


async function carregarLogs() {

    const resposta =
        await fetch("/api/logs");

    const logs =
        await resposta.json();

    document.getElementById(
        "logs-box"
    ).innerHTML =
        logs.join("<br>");
}

async function adicionarImagem() {

    const campo =
        document.getElementById(
            "nova-imagem"
        );

    const imagem =
        campo.value.trim();

    if (!imagem) {
        return;
    }

    await fetch(
        "/api/images",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
                imagem: imagem
            })
        }
    );

    campo.value = "";

    carregarImagens();
}


async function removerImagem(imagem) {

    await fetch(
        `/api/images/${encodeURIComponent(imagem)}`,
        {
            method: "DELETE"
        }
    );

    carregarImagens();
}

let intervaloInicializado = false;

async function carregarRuntime() {

    const resposta =
        await fetch("/api/runtime");

    const runtime =
        await resposta.json();

    if (!intervaloInicializado) {

        document.getElementById(
            "intervalo"
        ).value =
            runtime.intervalo;

        intervaloInicializado = true;
    }

    const statusTexto =
    document.getElementById(
        "status-monitoramento"
    );

    const statusCard =
        document.getElementById(
            "status-card"
        );

    if (runtime.monitorando) {

        statusTexto.innerText = "Ativo";

        statusCard.classList.remove(
            "parado"
        );

        statusCard.classList.add(
            "ativo"
        );

    }
    else {

        statusTexto.innerText = "Parado";

        statusCard.classList.remove(
            "ativo"
        );

        statusCard.classList.add(
            "parado"
        );
    }

}

async function iniciarMonitoramento() {

    const intervalo =
        parseInt(
            document.getElementById(
                "intervalo"
            ).value
        );

    await fetch(
        "/api/runtime",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
                monitorando: true,
                intervalo: intervalo
            })
        }
    );

    await carregarRuntime();
}


async function pararMonitoramento() {

    const intervalo =
        parseInt(
            document.getElementById(
                "intervalo"
            ).value
        );

    await fetch(
        "/api/runtime",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
                monitorando: false,
                intervalo: intervalo
            })
        }
    );

    await carregarRuntime();
}