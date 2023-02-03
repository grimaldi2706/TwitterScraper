
# TwitterScraper

#### Este código es una aplicación web escrita en Python utilizando la librería Flask y snscrape. Esta aplicación tiene la capacidad de recopilar tweets a través de técnicas de scraping(Scraping es un proceso de extracción de datos en línea), proporcionando una forma eficiente y sencilla de acceder a la información publicada en Twitter. 

#### La aplicación tiene 2 rutas principales:

1. "/": la ruta principal que renderiza el archivo "index.html".
2. "/ver_data": la ruta que maneja una solicitud POST y extrae tweets de Twitter utilizando la función get_tweets de la biblioteca "gettweets". La consulta y la cantidad de tweets se obtienen de los datos del formulario enviado. Los datos se guardan en un dataframe y se renderizan en el archivo "ver_data.html".

#### La biblioteca "gettweets" tiene la función de obtener tweets con una consulta específica y un límite de cantidad:

La función "get_tweets" toma como entrada una consulta y un límite de cantidad, y utiliza el módulo TwitterSearchScraper de la biblioteca snscrape para buscar tweets en Twitter que coincidan con la consulta especificada. Se extraen los datos relevantes de cada tweet y se agrega a una lista de tweets. Luego, se crea un DataFrame a partir de esta lista y se ordena por la columna "likeCount" en orden descendente.

Esta biblioteca se integra con la librería Pandas, lo que permite almacenar los datos extraídos en un DataFrame de Pandas y con ello manipularlos más fácilmente.

### Requiremientos
snscrape requiere Python 3.8 or inferior.

### by Grimaldi ✒️
