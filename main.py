import gettweets
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
#Instancia de Flask
app = Flask(__name__)


#Rutas:
#Ruta principal:
@app.route('/')
def incio():
  return render_template('index.html')


@app.route('/ver_data', methods=["POST"])
def ver_data():
  if request.method == 'POST':
    query = request.form["consulta"]
    valor = int(request.form["cantidad"])
    df = gettweets.get_tweets(query, limit=valor)
    df_u = df[['username']].reset_index(drop=True)
  return render_template("ver_data.html",
                         tabla=df.to_html(),
                         df_u=df.describe().to_html())


@app.route('/test/<query>/<int:valor>')
def data(query, valor):
  df = gettweets.get_tweets(query, limit=valor)
  df_u = df[['username']].reset_index(drop=True)
  return render_template("data.html", value=df.to_html())


#Iniciar el servidor:
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=80)
