import socket
import tweepy

HOST = 'localhost'
PORT = 9009

s = socket.socket()
s.bind((HOST, PORT))
print(f'Aguardando conexão na porta: {PORT}')

s.listen(5)

conn, address = s.accept()
print(f'Recebendo solicitação de: {address}')

# Utilizando token do twitter developer
token = 'AAAAAAAAAAAAAAAAAAAAANOAjwEAAAAAfb%2FWO1%2B4ijGQ0MPQJKaga4xQqXQ%3DmWy9Wrf2so02QK5M7Y7qvmzFgZFiPjnEtZczOfOY3VYjDEeN55'
# Palavra para filtrar no twitter
keyword = 'UOL'


class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        conn.send((tweet.text).encode('utf-8', 'ignore'))


printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

conn.close()
