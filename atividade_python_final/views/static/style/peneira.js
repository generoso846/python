/* Peneira de status da listagem de tarefas (sem recarregar a página) */
(function () {
    var seletor = document.getElementById("peneira-status");
    var painel = document.getElementById("painel-tarefas");
    var recadoVazio = document.getElementById("aviso-sem-registro");
    if (!seletor || !painel) return;

    var corpo = painel.querySelector("tbody");

    function classeMarcador(status) {
        return "marcador marcador-" + status.toLowerCase().replace(/\s+/g, "-");
    }

    function desenhar(lista) {
        corpo.innerHTML = "";
        lista.forEach(function (tar) {
            var linha = document.createElement("tr");
            linha.dataset.situacao = (tar.status || "").toLowerCase();
            linha.innerHTML =
                "<td></td><td></td><td><span></span></td><td></td>" +
                '<td><div class="coluna-comandos">' +
                '<a class="chave-vazada" href="/tarefa/editar/' + tar.id + '">Editar</a>' +
                '<a class="chave-risco" href="/tarefa/excluir/' + tar.id + '">Excluir</a>' +
                "</div></td>";
            var celulas = linha.querySelectorAll("td");
            celulas[0].textContent = tar.titulo;
            celulas[1].textContent = tar.descricao;
            var selo = celulas[2].querySelector("span");
            selo.className = classeMarcador(tar.status || "");
            selo.textContent = tar.status;
            celulas[3].textContent = tar.usuario || "—";
            corpo.appendChild(linha);
        });

        painel.hidden = lista.length === 0;
        if (recadoVazio) recadoVazio.hidden = lista.length !== 0;
    }

    function peneirar() {
        fetch("/api/v1/tarefas?status=" + encodeURIComponent(seletor.value))
            .then(function (r) { return r.json(); })
            .then(desenhar)
            .catch(function () { /* mantém a tabela renderizada pelo servidor */ });
    }

    seletor.addEventListener("change", peneirar);
})();
