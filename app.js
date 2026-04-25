async function fetchRepos() {
  try {
    const response = await fetch("https://api.github.com/users/tsichero/repos");
    const repos = await response.json();

    const container = document.getElementById("repos");
    container.innerHTML = "";

    repos.forEach(repo => {
      const div = document.createElement("div");

      div.innerHTML = `
        <h3>${repo.name}</h3>
        <p>${repo.description || "Sem descrição"}</p>
        <p><strong>Linguagem:</strong> ${repo.language || "N/A"}</p>
        <a href="${repo.html_url}" target="_blank">Ver no GitHub</a>
        <hr/>
      `;

      container.appendChild(div);
    });

  } catch (error) {
    document.getElementById("repos").innerHTML = "Erro ao carregar os repositórios 😢";
  }
}

fetchRepos();
