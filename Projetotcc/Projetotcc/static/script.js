async function adicionarProduto() {
    const nome = document.getElementById("nomeProduto").value;
    const quantidade = document.getElementById("quantidadeProduto").value;
    const foto = document.getElementById("linkFoto").value;

    if (!nome || !quantidade) {
        alert("Preencha o nome e a quantidade!");
        return;
    }

    try {
        const resposta = await fetch('/api/estoque', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nome, quantidade, foto })
        });

        const resultado = await resposta.json();
        if (resultado.sucesso) {
            alert(resultado.mensagem);
            // Limpa os campos
            document.getElementById("nomeProduto").value = "";
            document.getElementById("quantidadeProduto").value = "";
            document.getElementById("linkFoto").value = "";
            // Recarrega a tabela se estiver na página
            carregarProdutos();
        } else {
            alert("Erro ao cadastrar: " + resultado.erro);
        }
    } catch (erro) {
        console.error("Erro na requisição:", erro);
    }
}

async function carregarProdutos() {
    try {
        const resposta = await fetch('/api/estoque');
        const resultado = await resposta.json();

        if (resultado.sucesso) {
            const produtos = resultado.dados;

            const tabelaHome = document.querySelector("#tabela-linda tbody");
            if (tabelaHome) {
                tabelaHome.innerHTML = "";
                produtos.forEach(p => {
                    tabelaHome.innerHTML += `
                        <tr>
                            <td>${p.nome}</td>
                            <td>${p.quantidade}</td>
                            <td>-</td>
                            <td>-</td>
                            <td><img src="${p.foto || ''}" width="50" style="border-radius: 5px;" onerror="this.style.display='none'"></td>
                        </tr>
                    `;
                });
            }

            const tabelaEstoque = document.getElementById("tabelaProdutos");
            if (tabelaEstoque) {
                tabelaEstoque.innerHTML = "";
                produtos.forEach(p => {
                    tabelaEstoque.innerHTML += `
                        <tr>
                            <td>${p.id}</td>
                            <td>${p.nome}</td>
                            <td>${p.quantidade}</td>
                            <td><a href="${p.foto}" target="_blank">Ver Link</a></td>
                            <td><button class="btn btn-danger btn-sm" onclick="deletarProduto(${p.id})">Excluir</button></td>
                        </tr>
                    `;
                });
            }
        }
    } catch (erro) {
        console.error("Erro ao carregar produtos:", erro);
    }
}

// Deletar produto
async function deletarProduto(id) {
    if (!confirm("Tem certeza que deseja remover este item?")) return;

    try {
        const resposta = await fetch(`/api/estoque/${id}`, { method: 'DELETE' });
        const resultado = await resposta.json();
        if (resultado.sucesso) {
            carregarProdutos();
        } else {
            alert("Erro ao deletar: " + resultado.erro);
        }
    } catch (erro) {
        console.error("Erro ao deletar:", erro);
    }
}

document.addEventListener("DOMContentLoaded", carregarProdutos);