import requests
import json
import pandas as pd
import mplfinance as mpl

url = 'https://api.mexc.com/api/v3/klines?symbol=GEVONUSDT&interval=1m&limit=500'
response = requests.get(url)
responseBodyJson = json.loads(response.text)

formattedCandlesData = []
for candle in responseBodyJson:
    x = {
        'time': candle[0],
        'open': float(candle[1]),
        'high': float(candle[2]),
        'low': float(candle[3]),
        'close': float(candle[4])
    }
    formattedCandlesData.append(x)
df = pd.json_normalize(formattedCandlesData)
df.time = pd.to_datetime(df.time, unit='ms')
df = df.set_index('time')
df = df[['open', 'high', 'low', 'close']]
print(df.head())
print(df.tail())

def standardize(fragment):
    values = fragment[['open', 'close']].values.flatten()
    min_val = values.min()
    max_val = values.max()
    if max_val - min_val == 0:
        return values * 0
    standardized = (values - min_val) / (max_val - min_val)
    return standardized
pattern = df.tail(10)
pattern_standardized = standardize(pattern)

window_size = 10
tolerance = 0.15

matched_fragment = None
matched_index = None

for i in range(0, len(df) - 2 * window_size):
    tested_fragment = df.iloc[i:i + window_size]
    tested_standardized = standardize(tested_fragment)
    differences = abs(pattern_standardized - tested_standardized)
    if all(differences <= tolerance):
        matched_fragment = tested_fragment
        matched_index = i
        break

if matched_fragment is not None:
    print("Znaleziono podobny fragment!")
    print("Indeks początku fragmentu:", matched_index)
    print("Czas początku fragmentu:", matched_fragment.index[0])
    print("Czas końca fragmentu:", matched_fragment.index[-1])

    mpl.plot(
        pattern,
        type="candle",
        title="Wzorzec - ostatnie 10 świec",
        style="yahoo",
        mav=(3)
    )

    mpl.plot(
        matched_fragment,
        type="candle",
        title="Znalezione podobne 10 świec",
        style="yahoo",
        mav=(3)
    )
else:
    print("Nie znaleziono dopasowania.")