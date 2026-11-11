from flask import Flask, render_template, jsonify, request, redirect, session
from flask_bcrypt import Bcrypt 
import mysql.connector

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "172909_segredo_do_almoxarifado"

def conectar_banco():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="172909", 
        port=3306,
        database="almoxarifado",
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )

# Rota para verificação de acesso
@app.before_request
def verificar_autenticacao():
    rotas_protegidas = ["/home", "/estoque"]
    if request.path in rotas_protegidas and "usuario" not in session:
        return redirect("/")

# Rota para navegação
@app.route("/")
def index():
    if "usuario" in session:
        return redirect("/home")
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("email") or request.form.get("usuario")
    senha = request.form.get("password") or request.form.get("senha")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
        conta = cursor.fetchone()
        cursor.close()
        conexao.close()

        if conta and bcrypt.check_password_hash(conta["senha_hash"], senha):
            session["usuario"] = conta["usuario"]
            return redirect("/home")
        
        return "Usuário ou senha incorretos!", 401
    except Exception as e:
        return f"Erro na autenticação: {str(e)}", 500

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        usuario = request.form.get("email") or request.form.get("usuario")
        senha = request.form.get("password") or request.form.get("senha")

        if not usuario or not senha:
            return "Campos obrigatórios ausentes!", 400

        senha_criptografada = bcrypt.generate_password_hash(senha).decode('utf-8')

        try:
            conexao = conectar_banco()
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO usuarios (usuario, senha_hash) VALUES (%s, %s)", (usuario, senha_criptografada))
            conexao.commit()
            cursor.close()
            conexao.close()
            
            session["usuario"] = usuario
            return redirect("/home")
        except Exception as e:
            return f"Erro no Banco de Dados: {str(e)}", 500

    return render_template("cadastro.html")

# Rotas de API para o estoque
@app.route('/api/estoque', methods=['GET'])
def listar_produtos():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return jsonify({"sucesso": True, "dados": produtos}), 200
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500

@app.route('/api/estoque', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json() or {}
    nome = dados.get('nome')
    quantidade = dados.get('quantidade')
    foto = dados.get('foto')
    
    if not nome or quantidade is None:
        return jsonify({"sucesso": False, "erro": "Campos obrigatórios ausentes!"}), 400
    
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (nome, quantidade, foto) VALUES (%s, %s, %s)", (nome, quantidade, foto))
        conexao.commit()
        id_gerado = cursor.lastrowid
        cursor.close()
        conexao.close()
        
        return jsonify({"sucesso": True, "mensagem": "Produto cadastrado com sucesso!", "id": id_gerado}), 201
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500

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
    dados = request.get_json() or {}
    nome = dados.get("nome")
    quantidade = dados.get("quantidade")
    foto = dados.get("foto")

    if not nome or quantidade is None:
        return jsonify({"sucesso": False, "erro": "Campos obrigatórios ausentes!"}), 400

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("UPDATE produtos SET nome = %s, quantidade = %s, foto = %s WHERE id = %s", (nome, quantidade, foto, id))
        conexao.commit()
        linhas_alteradas = cursor.rowcount
        cursor.close()
        conexao.close()
        
        if linhas_alteradas == 0:
            return jsonify({"sucesso": False, "erro": "Item não encontrado!"}), 404
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
        linhas_deletadas = cursor.rowcount
        cursor.close()
        conexao.close()
        
        if linhas_deletadas == 0:
            return jsonify({"sucesso": False, "erro": "Item não encontrado!"}), 404
        return jsonify({"sucesso": True, "mensagem": "Item removido com sucesso!"}), 200
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)