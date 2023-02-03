import snscrape.modules.twitter as sntwitter
import pandas as pd


# Función para obtener tweets con una consulta específica y un límite de cantidad
def get_tweets(query, limit=10):
  # Lista para almacenar los tweets
  tweets = []

  for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # Si se alcanzó el límite de cantidad de tweets, detener el ciclo
    if len(tweets) == limit:
      break
    else:
      # Agregar los datos de cada tweet a la lista de tweets
      tweets.append([
        tweet.conversationId, tweet.date, tweet.user.username,
        tweet.sourceLabel, tweet.user.location, tweet.likeCount,
        tweet.retweetCount, tweet.replyCount, tweet.url, tweet.content
      ])
  # Crear un DataFrame a partir de la lista de tweets con los nombres de columna especificados
  df = pd.DataFrame(tweets,
                    columns=[
                      'conversationId', 'date', 'username', 'Source',
                      'Location', 'likeCount', 'retweetCount', 'replyCount',
                      'url', 'content'
                    ])

  df_u = df[['username']]

  # Ordenar el DataFrame principal por la columna "likeCount" en orden descendente
  return df.sort_values(by='likeCount', ascending=False)


def check_verified():
  username = "grimaldi93"
  user_info = next(sntwitter.TwitterUserScraper(username).get_items())
  return print(user_info.isVerified)
