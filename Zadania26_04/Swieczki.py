import requests
import json
import pandas as pd
import mplfinance as mpl
url = 'https://api.mexc.com/api/v3/klines?symbol=GEVONUSDT&interval=30m&limit=10' # url z danymi na temat świeczek (Postman)
response = requests.get(url) # pobiera zasób z url
responseBody = response.text # obiekt response zawiera atrybut "text", z naszymi danymi (całe response zawiera jeszcze dodatkowo metadane zapytania, które nie są nam potrzebne)
responseBodyJson = json.loads(responseBody) # przetwarzamy tekst w formacie json
print(responseBodyJson)
formattedCandlesData=[]
for candle in responseBodyJson:
   x = {
       'time': candle[0],
       'open': float(candle[1]),
       'close': float(candle[4]),
       'high': float(candle[2]),
       'low': float(candle[3])
   }
   formattedCandlesData.append(x)

df=pd.json_normalize(formattedCandlesData)
df.time = pd.to_datetime(df.time, unit='ms')
df=df.set_index('time')
print(df.columns)
# wyświetlanie tego atrybutu zwróci nam listę kolumn - "Index(['open', 'close', 'high', 'low'], dtype='object')"
print(df.head())
# funkcja head wywołana na obiekcie df pozwoli nam wyświetlić podgląd naszych danych wraz z nagłówkami
mpl.plot(
    df,
    type="candle", # typ wykresu
    title="Candle chart", # tytuł
    style="yahoo", # wersja kolorystyczna 
    mav=(3, 6, 9) # automatyczne obliczanie oraz rysowanie średni kroczących
)