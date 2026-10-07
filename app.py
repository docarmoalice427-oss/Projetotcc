from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

def conectar_banco():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="172909",
        database="almoxarifado"
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")


############# Rotas api

@app.route("/api/estoque/<int:id>", methods=["GET"])
def obter_item_estoque(id):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
        item = cursor.fetchone()
        cursor.close()
        conexao.close()
        
        if not item:
            return jsonify({"sucesso": False, "erro": "Item não encontrado!"}), 404
            
        return jsonify({"sucesso": True, "dados": item}), 200
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500

@app.route("/api/estoque/<int:id>", methods=["PUT"])
def atualizar_item_estoque(id):
    dados = request.get_json()
    nome = dados.get("nome")
    quantidade = dados.get("quantidade")
    preco = dados.get("preco")

    if not nome or quantidade is None:
        return jsonify({"sucesso": False, "erro": "Campos 'nome' e 'quantidade' são obrigatórios!"}), 400

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        sql = "UPDATE produtos SET nome = %s, quantidade = %s, preco = %s WHERE id = %s"
        cursor.execute(sql, (nome, quantidade, preco, id))
        conexao.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            conexao.close()
            return jsonify({"sucesso": False, "erro": "Item não encontrado!"}), 404
            
        cursor.close()
        conexao.close()
        return jsonify({"sucesso": True, "mensagem": "Item atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500

@app.route("/api/estoque/<int:id>", methods=["DELETE"])
def deletar_item_estoque(id):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
        conexao.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            conexao.close()
            return jsonify({"sucesso": False, "erro": "Item não encontrado!"}), 404
            
        cursor.close()
        conexao.close()
        return jsonify({"sucesso": True, "mensagem": "Item removido com sucesso!"}), 200
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500

if __name__ == '__main__':
    app.app_context().push()
    app.run(host='0.0.0.0', port=5000, debug=True)      

################ 

    from flask import Flask, request, jsonify

@app.route('/api/estoque', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()
    nome = dados.get('nome')
    quantidade = dados.get('quantidade')
    preco = dados.get('preco')
    
    
    conexao = obter_conexao() 
    cursor = conexao.cursor()
    sql = "INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, quantidade, preco))
    conexao.commit()
    
    id_gerado = cursor.lastrowid
    cursor.close()
    conexao.close()
    
    return jsonify({
        "sucesso": True, 
        "mensagem": "Produto cadastrado com sucesso!",
        "id": id_gerado
    }), 201