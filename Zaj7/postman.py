import requests
import json
import pandas as pd
import mplfinance as mpl

url = 'https://api.mexc.com/api/v3/klines?symbol=GEVONUSDT&interval=30m&limit=10'

response = requests.get(url)
respondeBody = response.text
respondeJson = json.loads(respondeBody)

print(respondeJson)
formattedCandlesData = []
for candle in respondeJson:
    x={
        'time': candle[0],
        'open': float(candle[1]),
        'close': float(candle[4]),
        'high': float(candle[2]),
        'low': float(candle[3])
    }
    formattedCandlesData.append(x)




df = pd.json_normalize(formattedCandlesData)  # przetwarzamy dane w formacie json
df.time = pd.to_datetime(df.time, unit='ms')  # ponieważ oczekiwany format daty w kolumnie "time" jest inny niż oczekiwany przez bibliotekę to musimy go skonwertować
df = df.set_index("time")  # ustawiamy index naszych danych na kolumnę "time"

print(df.columns) # wyświetlanie tego atrybutu zwróci nam listę kolumn - "Index(['open', 'close', 'high', 'low'], dtype='object')"
print(df.head()) # funkcja head wywołana na obiekcie df pozwoli nam wyświetlić podgląd naszych danych wraz z nagłówkami


mpl.plot(
    df, # przekazujemy obiekt z danymi
    type="candle", # określamy typ wykresu
    title="Candle chart", # nadajemy tytuł naszego wykresu
    style="yahoo", # wersja kolorystyczna naszego wykresu - inne to np. binance, blueskies, brasil, charles, checkers, classic, default, mike, nightclouds, sas, starsandstripes
    mav=(3, 6, 9) # atrybut który włączy automatyczne obliczanie oraz rysowanie średni kroczących
)


