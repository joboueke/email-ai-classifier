const API_URL = "";

function showLoading(show) {
    document.getElementById("loading").classList.toggle("hidden", !show);
}

function showResult(data) {
    const result = document.getElementById("result");
    const badge = document.getElementById("category");

    result.classList.remove("hidden");

    badge.innerText = data.categoria;
    badge.className = "badge " + data.categoria.toLowerCase();

    document.getElementById("response").innerText = data.resposta_sugerida;
}

function classifyText() {
    const text = document.getElementById("emailText").value;

    if (!text) {
        alert("Digite o texto do email.");
        return;
    }

    showLoading(true);

    fetch(`${API_URL}/classify-email`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: text })
    })
    .then(res => res.json())
    .then(data => {
        showLoading(false);
        showResult(data);
    })
    .catch(() => {
        showLoading(false);
        alert("Erro ao processar o email.");
    });
}

function uploadFile() {
    const fileInput = document.getElementById("fileInput");

    if (!fileInput.files.length) {
        alert("Selecione um arquivo.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    showLoading(true);

    fetch(`${API_URL}/upload-email`, {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        showLoading(false);
        showResult(data);
    })
    .catch(() => {
        showLoading(false);
        alert("Erro ao enviar arquivo.");
    });
}
