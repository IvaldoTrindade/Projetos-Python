from flask import Flask, request, jsonify

app = Flask(__name__)

musicas = [
    {
        'nome':'I Know',
        'autor':'Travis Scott'
    },
    {
        'nome':'0 to 100',
        'autor':'Drake'
    },
    {
        'nome':"They don't like us",
        'autor':'Kendrick Lamar'
    }
]

#GET
@app.route('/cancoes')
def capturar_musica():
    return jsonify(musicas)

#GET com id
@app.route('/cancoes/<int:indice>',methods=["GET"])
def capturar_musica_com_id(indice):
    return jsonify(musicas[indice])

#POST
@app.route('/cancoes',methods=['POST'])
def inserir_musica():
    cancao = request.get_json()
    musicas.append(cancao)
    return jsonify(cancao, 200)

#PUT
@app.route('/cancoes/<int:indice>',methods=['PUT'])
def alterar_musica(indice):
    cancao = request.get_json()
    musicas[indice].update(cancao)
    return jsonify(musicas[indice],200)

#DELETE 
@app.route('/cancoes/<int:indice>',methods=['DELETE'])
def deletar_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Foi excluída a música{musicas[indice]}.', 200) 
    except:
        return jsonify(f'Não há nenhuma música com esse índice.', 404) 
    
app.run(port=5000,host='localhost',debug=True)