# TwitterScraper

### Este código es una aplicación web escrita en Python utilizando la librería Flask. La aplicación tiene tres rutas principales:

1. "/": la ruta principal que renderiza el archivo "index.html".
2. "/ver_data": la ruta que maneja una solicitud POST y extrae tweets de Twitter utilizando la función get_tweets de la biblioteca "gettweets". La consulta y la cantidad de tweets se obtienen de los datos del formulario enviado. Los datos se guardan en un dataframe y se renderizan en el archivo "ver_data.html".
