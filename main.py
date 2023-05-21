from flask import Flask, request, jsonify
from crawler.primeira_instancia import primeiraInstancia
from crawler.segunda_instancia import segundainstancia
import json

app = Flask(__name__)

@app.route("/processo", methods=["POST"])
def processar_processo():
    data = request.get_json()
    processo = data.get("processo")

    if processo:
        crawler1 = primeiraInstancia(processo)
        dados = crawler1.buscar_dados()
        crawler2 = segundainstancia(processo)
        dados2 = crawler2.buscar_dados()
        if dados:
            classe, area, assunto, distribuicao, juiz, valor, nomes, moviment = dados
            if dados2 != None:
                classe2, assunto2, relator2, moviment2 = dados2
                if valor != None:
                    valor = valor.replace(" ", "")

                data = {
                    "1---Instância---": "Primeira instância",
                    "1Classe": classe,
                    "1Área": area,
                    "1Assunto": assunto,
                    "1Distribuição": distribuicao,
                    "1Juiz": juiz,
                    "1valor": valor,
                    "1partes": nomes,
                    "1Movimentações": moviment,
                    "2-------Instância--------": "segunda instância",
                    "2Classe_segunda": classe2,
                    "2Assunto_segunda": assunto2,
                    "2Relator": relator2,
                    "2Movimentações_segunda": moviment2
                }
            else:
                if valor != None:
                    valor = valor.replace(" ", "")

                data = {
                    "---Instância---": "primeira instância",
                    "Classe": classe,
                    "Área": area,
                    "Assunto": assunto,
                    "Distribuição": distribuicao,
                    "Juiz": juiz,
                    "valor": valor,
                    "partes": nomes,
                    "Movimentações": moviment,
                    "Mensagem": "Esse processo não tem segunda instância",
                }
            dados_json = json.dumps(data, ensure_ascii=False)

            with open("dados.json", "w", encoding="utf8") as arquivo:
                arquivo.write(dados_json)
            with open(r"C:\Users\Notebook\Desktop\Teste_JusBrasil\dados.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            return jsonify(dados), 200

        else:
            return jsonify({"Erro": "Erro ao buscar dados do processo."}), 500
    else:
        return jsonify({"Erro": "Processo vazio"}), 400
if __name__ == "__main__":
    app.run()