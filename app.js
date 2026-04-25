async function fetchRepos() {
  try {
    const response = await fetch("https://api.github.com/users/tsichero/repos");
    const repos = await response.json();

    const container = document.getElementById("repos");
    container.innerHTML = "";

    // 🔥 Função de Score
    function getScore(repo) {
      return (repo.stargazers_count * 2) + repo.forks_count;
    }

    repos.forEach(repo => {
      const div = document.createElement("div");

      // 👇 aplica o estilo de card
      div.classList.add("card");

      div.innerHTML = `
        <h3>${repo.name}</h3>
        <p>${repo.description || "Sem descrição"}</p>
        <p><strong>Linguagem:</strong> ${repo.language || "N/A"}</p>
        <p><strong>Score:</strong> ${getScore(repo)}</p>
        <a href="${repo.html_url}" target="_blank">Ver no GitHub</a>
      `;

      container.appendChild(div);
    });

  } catch (error) {
    document.getElementById("repos").innerHTML = "Erro ao carregar os repositórios 😢";
    console.error(error);
  }
}

fetchRepos();
