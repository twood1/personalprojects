import gdax, time
import http.client

class Ticker:
    def __init__(self,type):
        public_client = gdax.PublicClient()
        public_client.get_product_ticker(product_id=type)

ticker = Ticker('ETH-USD')
wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="ETH-USD")

f = open("D:/MEW/SapkGDX.txt")
lines = f.readlines()
b64secret = lines[0]

f = open("D:/MEW/apk.txt")
lines = f.readlines()
key = lines[0].strip()
passphrase = lines[1].strip()

auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)

order_book = gdax.OrderBook(product_id='ETH-USD')
order_book.start()

time.sleep(2)
prevbook = order_book.get_current_book()
file = open("C:/Users/Tim/Desktop/testfile.txt","w+")


i = 0
while i < 1000:
    i += 1

    book = order_book.get_current_book()
    #print(prevbook == book)
    prevbook = book


    file.write("ASKS__________\n")

    for ele in book['asks']:
        file.write(str(ele)+"\n")

    file.write("BUYS__________\n")
    for ele in book['bids']:
        file.write(str(ele)+"\n")

    file.write("___________________________________________\n")


order_book.close()
#while True:
#    currBook = order_book.get_current_book()
#    time.sleep(2)
#    print("hi?")




