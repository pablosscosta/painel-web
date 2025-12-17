const painel = document.getElementById("painel");
const atualizacao = document.getElementById("atualizacao");

const source = new EventSource("/stream");

source.onmessage = function(event) {
  const data = JSON.parse(event.data);

  painel.textContent = data.valor;
  atualizacao.textContent = `Última atualização: ${data.modificado}`;

  painel.classList.add("atualizado");
  setTimeout(() => painel.classList.remove("atualizado"), 500);
};
