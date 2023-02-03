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
  """
  Esta función se activa cuando se hace una solicitud HTTP POST a la ruta '/ver_data'.
  """
  if request.method == 'POST':
    # Obtiene la consulta y la cantidad desde los datos del formulario enviados en la solicitud HTTP POST.
    query = request.form["consulta"]
    valor = int(request.form["cantidad"])
    # Llama a la función get_tweets de la libreria gettweets para obtener los tweets según la consulta y la cantidad especificadas.
    df = gettweets.get_tweets(query, limit=valor)
    df_u = df[['username']].reset_index(drop=True)
  # Renderiza la plantilla 'ver_data.html' y pasa las variables df (con los datos de los tweets) y df_u (con la descripción estadística de los usuarios) a la plantilla.
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
