const API = "http://127.0.0.1:8000";


const formulario = document.getElementById(
    "formChamado"
);


if (formulario) {

    formulario.addEventListener(
        "submit",
        cadastrarChamado
    );

}


async function cadastrarChamado(event) {

    event.preventDefault();

    const titulo = document.getElementById(
        "titulo"
    ).value;

    const descricao = document.getElementById(
        "descricao"
    ).value;

    const status = document.getElementById(
        "status"
    ).value;


    const dados = {
        titulo: titulo,
        descricao: descricao,
        status: status
    };


    try {

        const resposta = await fetch(
            `${API}/chamados`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(dados)
            }
        );


        const resultado = await resposta.json();


        if (!resposta.ok) {

            mostrarMensagem(
                "Erro ao cadastrar chamado."
            );

            return;
        }


        mostrarMensagem(
            "Chamado cadastrado com sucesso!"
        );


        formulario.reset();

        carregarChamados();

    } catch (erro) {

        mostrarMensagem(
            "Não foi possível conectar à API."
        );

        console.error(erro);
    }
}


async function carregarChamados() {

    const lista = document.getElementById(
        "listaChamados"
    );


    if (!lista) {
        return;
    }


    try {

        const resposta = await fetch(
            `${API}/chamados`
        );


        const chamados = await resposta.json();


        lista.innerHTML = "";


        if (chamados.length === 0) {

            lista.innerHTML =
                "<p>Nenhum chamado cadastrado.</p>";

            return;
        }


        chamados.forEach(function(chamado) {

            const div = document.createElement(
                "div"
            );

            div.className = "chamado";


            div.innerHTML = `
                <h3>#${chamado.id} - ${chamado.titulo}</h3>

                <p>
                    ${chamado.descricao}
                </p>

                <p>
                    <strong>Status:</strong>
                    ${chamado.status}
                </p>

                <p>
                    <strong>Criado em:</strong>
                    ${chamado.criado_em}
                </p>

                <button onclick="excluirChamado(${chamado.id})">
                    Excluir
                </button>
            `;


            lista.appendChild(div);

        });

    } catch (erro) {

        lista.innerHTML =
            "<p>Erro ao carregar chamados.</p>";

        console.error(erro);
    }
}


async function excluirChamado(id) {

    const confirmar = confirm(
        "Deseja excluir este chamado?"
    );


    if (!confirmar) {
        return;
    }


    try {

        const resposta = await fetch(
            `${API}/chamados/${id}`,
            {
                method: "DELETE"
            }
        );


        if (resposta.ok) {

            alert(
                "Chamado excluído com sucesso!"
            );

            carregarChamados();

        } else {

            alert(
                "Erro ao excluir chamado."
            );
        }

    } catch (erro) {

        alert(
            "Não foi possível conectar à API."
        );

        console.error(erro);
    }
}


function mostrarMensagem(texto) {

    const mensagem = document.getElementById(
        "mensagem"
    );


    if (mensagem) {

        mensagem.textContent = texto;

    }
}


carregarChamados();