fetch("http://127.0.0.1:5000/api/dados")
  .then(response => response.json())
  .then(data => {

    const div = document.getElementById("dados");

    div.innerHTML = `<p>Valor: ${data[0]}</p>`;
  })
  .catch(error => {
    console.error("Erro ao buscar dados:", error);
  });
