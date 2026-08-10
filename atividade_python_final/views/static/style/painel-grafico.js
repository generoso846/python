/* Frase do dia (API pública) + gráfico rosca com Chart.js */
(function () {
    var alvoFrase = document.getElementById("citacao-dia");
    if (alvoFrase && alvoFrase.dataset.buscar === "sim") {
        fetch("https://api.adviceslip.com/advice")
            .then(function (r) { return r.json(); })
            .then(function (dados) { alvoFrase.textContent = dados.slip.advice; })
            .catch(function () { alvoFrase.textContent = "Não foi possível carregar a frase de hoje."; });
    }

    var tela = document.getElementById("tela-rosca");
    if (!tela || typeof Chart === "undefined") return;

    fetch("/api/v1/tarefas/status")
        .then(function (r) { return r.json(); })
        .then(function (dados) {
            var numeros = [
                dados.pendente || 0,
                dados["em andamento"] || 0,
                dados.concluida || 0
            ];

            var tudoZero = numeros.every(function (v) { return v === 0; });
            if (tudoZero) {
                tela.hidden = true;
                var vazio = document.getElementById("rosca-sem-dados");
                if (vazio) vazio.hidden = false;
                return;
            }

            new Chart(tela, {
                type: "doughnut",
                data: {
                    labels: ["Pendente", "Em andamento", "Concluída"],
                    datasets: [{
                        data: numeros,
                        backgroundColor: ["#f59f00", "#2563eb", "#15803d"],
                        borderColor: "#1b1a17",
                        borderWidth: 3
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    cutout: "58%",
                    plugins: {
                        legend: {
                            position: "bottom",
                            labels: { boxWidth: 14, font: { size: 12, weight: "bold" } }
                        }
                    }
                }
            });
        })
        .catch(function () { tela.hidden = true; });
})();
