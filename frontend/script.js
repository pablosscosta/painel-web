function atualizarPainel() {
  fetch("/api/dados")
    .then(response => response.json())
    .then(data => {
      document.getElementById("painel").textContent = data.valor;
      document.getElementById("atualizacao").textContent = `Última atualização: ${data.modificado}`;
    })
    .catch(error => {
      document.getElementById("painel").textContent = "Erro";
      console.error("Erro:", error);
    });
}


atualizarPainel();


setInterval(atualizarPainel, 900000);
