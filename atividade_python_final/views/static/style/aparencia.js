/* Alternador de aparência (claro / noturno) */
(function () {
    var CHAVE_MEMORIA = "neobrutal-board-aparencia";
    var botao = document.getElementById("gatilho-lampada");

    function pintar(modo) {
        var noturno = modo === "noturno";
        document.body.classList.toggle("modo-noturno", noturno);
        if (botao) {
            botao.textContent = noturno ? "☀" : "☾";
            botao.setAttribute("aria-label", noturno ? "Ativar modo claro" : "Ativar modo noturno");
        }
    }

    pintar(localStorage.getItem(CHAVE_MEMORIA) || "claro");

    if (botao) {
        botao.addEventListener("click", function () {
            var proximo = document.body.classList.contains("modo-noturno") ? "claro" : "noturno";
            localStorage.setItem(CHAVE_MEMORIA, proximo);
            pintar(proximo);
        });
    }
})();
